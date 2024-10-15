from django.shortcuts import render


def home(request):
    return render(request, "job_me/home.html")


def categories(request):
    return render(request, "job_me/categories.html")


def about(request):
    return render(request, "job_me/about.html")


def custom_404(request, exception):
    return render(request, '404.html', status=404)


def custom_500(request):
    return render(request, '500.html', status=500)