from django import forms

from petstagram.main.helpers import BootstrapFormMixin
from petstagram.main.models import Profile


class ProfileForm(BootstrapFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_control()

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'profile_picture')
        widgets={
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name'
                }
            ),
            'profile_picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL'
                }
            ),
        }