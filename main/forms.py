from django import forms
from django.forms import ModelForm

from main.models import Contact

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder, Div, \
    MultiField

class ContactForm(ModelForm):

    name = forms.CharField(
        label = "Full Name",
    )
    message = forms.CharField(
        widget = forms.Textarea,
    )

    class Meta:
        model = Contact

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'contact-form'
        self.helper.form_class = 'submission-form'
        self.helper.layout = Layout(
            Fieldset(
                'You\'re just one email away',
                Div('name',
                    css_class = 'col-xs-6'
                ),
                Div('email',
                    css_class = 'col-xs-6'
                ),
                Div('company',
                    css_class = 'col-xs-6',
                ),
                Div('skype',
                    css_class = 'col-xs-6',
                ),
                'message'
            ),
            ButtonHolder(
                Submit('submit', 'Send', css_class='btn-info btn-lg')
            )
        )
