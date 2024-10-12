from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import UserProfileForm


def home(request):
    return render(request, "base.html")


@login_required
def profile(request):
    """Display the user's profile."""
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
        else:
            messages.error(request, "Update failed. Please ensure the form is valid.")
    else:
        form = UserProfileForm(instance=profile)

    context = {
        "form": form,
        "on_profile_page": True,
    }

    return render(request, "profiles/profile.html", context)
