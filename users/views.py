from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages


@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect("profile")
    else:
        form = UserProfileForm(instance=user_profile)

    context = {
        "form": form,
    }

    return render(request, "users/profile.html", context)


def custom_logout(request):
    logout(request)
    return redirect("job_me:home")
