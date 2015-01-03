from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Div, ButtonHolder

from .models import Post


class PostBaseForm(forms.ModelForm):
    '''
    Base form to be inherited by other blog post forms
    '''

    # set the text at the top of the form
    form_title = ""

    class Meta:
        model = Post
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(PostBaseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                self.form_title,
                Div(
                    Div('title', css_class="col-sm-6"),
                    Div('tags', css_class="col-sm-6"),
                    css_class="row"
                ),
                'heading',
                'body',
                'active',
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn btn-primary')
            )
        )


class PostCreateForm(PostBaseForm):
    '''
    Create a new blog post
    '''

    form_title = "<h1 class='text-center'>Create New Post</h1>"


class PostUpdateForm(PostBaseForm):
    '''
    Update an existing blog post
    '''

    form_title = "<h1 class='text-center'>Update Blog Post</h1>"

