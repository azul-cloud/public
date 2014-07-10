from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings

from main.models import Trait, Example
from main.forms import ContactForm

# Create your views here.
def home(request):
    traits = Trait.objects.all()
    examples = Example.objects.all()
    template = 'main/content/home.html'

    #shared dictionary with static view variables
    render_dict = {'traits':traits, 'examples':examples}

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            email = EmailMessage('Azul Cloud Contact',
                cd["message"],
                settings.EMAIL_HOST_USER,
                ['awwester@gmail.com'],
                headers = {'Reply-To': cd["email"]})

            email.send()
            form.save()
            load_modal = "sentModal"
            form = ContactForm()
        else:
            load_modal = "errorModal"

        return render(request, template,
            dict(render_dict, **{'form':form, 'load_modal':load_modal}))
    else:
        form = ContactForm()
        load_modal = None

        return render(request, template, dict(render_dict, **{'form':form, 'load_modal':load_modal}))