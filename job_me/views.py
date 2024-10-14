from django.shortcuts import render, get_object_or_404
from .models import Category, Technology, Topic


def home(request):
    return render(request, "job_me/home.html")


def categories(request):
    return render(request, "job_me/categories.html")


def about(request):
    return render(request, "job_me/about.html")


def category_list(request):
    categories = Category.objects.prefetch_related("technologies").all()
    return render(request, "job_me/category_list.html", {"categories": categories})


def technology_detail(request, technology_id):
    technology = get_object_or_404(Technology, id=technology_id)

    # Get all modules related to this technology
    modules = technology.modules.all()

    return render(
        request,
        "job_me/technology_detail.html",
        {"technology": technology, "modules": modules},
    )
