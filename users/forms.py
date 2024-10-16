from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile

        fields = [
            "first_name",
            "last_name",
            "bio",
            "avatar",
            "github",
            "linkedin",
            "twitter",
            "phone",
            "mobile",
            "address",
        ]

        widgets = {
            "bio": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Tell us about yourself...",
                }
            ),
            "github": forms.URLInput(
                attrs={"class": "form-control", "placeholder": "GitHub profile URL"}
            ),
            "linkedin": forms.URLInput(
                attrs={"class": "form-control", "placeholder": "LinkedIn profile URL"}
            ),
            "twitter": forms.URLInput(
                attrs={"class": "form-control", "placeholder": "Twitter profile URL"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Phone number"}
            ),
            "mobile": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Mobile number"}
            ),
            "address": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your address"}
            ),
        }
