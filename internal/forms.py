from django import forms
from django.forms import ModelForm

from internal.models import Task

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder, Div


class TaskForm(ModelForm):

    class Meta:
        model = Task

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                "project",
                "title",
                "description",
                "dev_notes",
                Div("status", css_class="col-md-6"),
                Div("assigned_to", css_class="col-md-6"),
                Div("complete_date", css_class="col-md-6"),
                Div("sent_date", css_class="col-md-6"),
                Div("notify_client", css_class="col-md-6"),
            ),
            ButtonHolder(
                Submit('submit', 'Save', css_class='btn-info btn-lg btn-block')
            )
        )