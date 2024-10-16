from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages
from job_me.models import UserTechnologyProgress, Technology


@login_required
def profile(request):

    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    tech_progress = UserTechnologyProgress.objects.filter(user=user_profile)
    technologies = Technology.objects.all()

    context = {
        "user_profile": user_profile,
        "tech_progress": tech_progress,
        "technologies": technologies,
    }

    return render(request, "users/profile.html", context)


@login_required
def update_profile(request):

    user_profile = request.user.userprofile

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect("/profile")
    else:
        form = UserProfileForm(instance=user_profile)

    return render(
        request,
        "users/profile_update.html",
        {"form": form, "user_profile": user_profile},
    )


def custom_logout(request):
    logout(request)
    return redirect("job_me:home")
