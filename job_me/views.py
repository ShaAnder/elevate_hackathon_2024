from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Technology, Module, Question, Topic


def home(request):
    return render(request, "job_me/home.html")


def categories(request):
    return render(request, "job_me/categories.html")


def about(request):
    return render(request, "job_me/about.html")


def category_list(request):
    categories = Category.objects.prefetch_related("technologies").all()
    return render(request, "job_me/category_list.html", {"categories": categories})


from django.shortcuts import get_object_or_404, render
from .models import Technology, Module, Question


def technology_detail(request, technology_id):

    technology = get_object_or_404(Technology, id=technology_id)

    # Prefetch related topics and questions
    modules = Module.objects.filter(technology=technology).prefetch_related(
        "topics__questions"
    )

    # Retrieve all questions related to the technology
    questions = Question.objects.filter(topic__module__technology=technology)

    # Context to pass to the template
    context = {
        "technology": technology,
        "modules": modules,
        "questions": questions,
    }

    # Render the template with the context
    return render(request, "job_me/technology_detail.html", context)


def question_list(request, technology_id):
    # Retrieve the technology by its ID
    technology = get_object_or_404(Technology, id=technology_id)

    # Get all the modules related to this technology
    modules = technology.modules.all()

    # Get all topics within the modules
    topics = Topic.objects.filter(module__in=modules)

    # Get all questions within the topics
    questions = Question.objects.filter(topic__in=topics)

    context = {
        "technology": technology,
        "questions": questions,
    }
    return render(request, "job_me/question_list.html", context)


def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    # Retrieve all questions related to the same technology
    questions = Question.objects.filter(
        topic__module__technology=question.topic.module.technology
    )

    context = {
        "question": question,
        "questions": questions,
    }

    return render(request, "job_me/question_detail.html", context)


def redirect_to_first_question_from_module(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    # Find the first question in the module (through its topics)
    first_question = (
        Question.objects.filter(topic__module=module).order_by("id").first()
    )

    if first_question:
        return redirect("job_me:question_detail", question_id=first_question.id)
    else:
        # Handle the case where no questions are found
        return redirect("job_me:technology_detail", technology_id=module.technology.id)


def redirect_to_first_question_from_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    # Find the first question in the topic
    first_question = Question.objects.filter(topic=topic).order_by("id").first()

    if first_question:
        return redirect("job_me:question_detail", question_id=first_question.id)
    else:
        # Handle the case where no questions are found
        return redirect(
            "job_me:technology_detail", technology_id=topic.module.technology.id
        )
