from django import forms
from django.forms import ModelForm

from .models import Project

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder, Div


class ProjectForm(ModelForm):
    class Meta:
        model = Project

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                "client",
                "title",
                "contacts",
                "description",
                "active",
                "pay_amount"
            ),
            ButtonHolder(
                Submit('submit', 'Update', css_class='btn-info btn-lg btn-block')
            )
        )