from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    """Display the user's profile."""
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserProfileForm(instance=profile)

    template = "users/profile.html"
    context = {
        "form": form,
        "on_profile_page": True,
    }

    return render(request, template, context)


def custom_logout(request):
    logout(request)
    return redirect("job_me:home")
