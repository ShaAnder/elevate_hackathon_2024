from django import forms
from .models import Profile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
