from django.shortcuts import render, get_object_or_404, redirect
from .models import (
    Category,
    Technology,
    Module,
    Question,
    Topic,
    UserTechnologyProgress,
    UserQuestionKnowledge,
)
from .forms import UserQuestionKnowledgeForm
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "job_me/home.html")


def categories(request):
    return render(request, "job_me/categories.html")


def about(request):
    return render(request, "job_me/about.html")


def custom_404(request, exception):
    return render(request, "404.html", status=404)


def custom_500(request):
    return render(request, "500.html", status=404)


def interview(request):
    return render(request, "job_me/interview.html")


def category_list(request):
    categories = Category.objects.prefetch_related("technologies")
    user_progress_dict = {}
    if request.user.is_authenticated:

        user_progress = UserTechnologyProgress.objects.filter(
            user=request.user.userprofile
        )

        for progress in user_progress:
            user_progress_dict[progress.technology.id] = progress.progress_percentage

    context = {
        "categories": categories,
        "user_progress_dict": user_progress_dict,
    }

    return render(request, "job_me/category_list.html", context)


@login_required
def technology_detail(request, technology_id):

    technology = get_object_or_404(Technology, id=technology_id)
    modules = Module.objects.filter(technology=technology).prefetch_related(
        "topics__questions"
    )

    user_progress = UserTechnologyProgress.objects.filter(
        user=request.user.userprofile, technology=technology
    ).first()

    context = {
        "technology": technology,
        "modules": modules,
        "user_progress": user_progress,
    }

    return render(request, "job_me/technology_detail.html", context)


def question_list(request, technology_id):

    technology = get_object_or_404(Technology, id=technology_id)
    modules = technology.modules.all()
    topics = Topic.objects.filter(module__in=modules)
    questions = Question.objects.filter(topic__in=topics)

    context = {
        "technology": technology,
        "questions": questions,
    }
    return render(request, "job_me/question_list.html", context)


def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    technology = question.topic.module.technology

    user_profile = request.user.userprofile

    user_question_knowledge, created = UserQuestionKnowledge.objects.get_or_create(
        user=user_profile, question=question
    )

    if request.method == "POST":
        form = UserQuestionKnowledgeForm(request.POST, instance=user_question_knowledge)
        if form.is_valid():
            form.save()
            progress_record, _ = UserTechnologyProgress.objects.get_or_create(
                user=user_profile,
                technology=technology,
            )
            progress_record.calculate_progress()
            return redirect("job_me:question_detail", question_id=question_id)
    else:
        form = UserQuestionKnowledgeForm(instance=user_question_knowledge)

    questions = list(
        Question.objects.filter(topic__module__technology=technology).order_by("id")
    )
    current_index = questions.index(question)

    next_question = (
        questions[current_index + 1] if current_index + 1 < len(questions) else None
    )
    previous_question = questions[current_index - 1] if current_index - 1 >= 0 else None

    context = {
        "question": question,
        "questions": questions,
        "next_question": next_question,
        "previous_question": previous_question,
        "technology": technology,
        "form": form,
    }

    return render(request, "job_me/question_detail.html", context)


def redirect_to_first_question_from_module(request, module_id):

    module = get_object_or_404(Module, id=module_id)
    first_question = (
        Question.objects.filter(topic__module=module).order_by("id").first()
    )

    if first_question:
        return redirect("job_me:question_detail", question_id=first_question.id)
    else:
        return redirect("job_me:technology_detail", technology_id=module.technology.id)


def redirect_to_first_question_from_topic(request, topic_id):

    topic = get_object_or_404(Topic, id=topic_id)
    first_question = Question.objects.filter(topic=topic).order_by("id").first()

    if first_question:
        return redirect("job_me:question_detail", question_id=first_question.id)
    else:
        return redirect(
            "job_me:technology_detail", technology_id=topic.module.technology.id
        )


def update_knowledge_status(request, question_id):
    if request.method == "POST":
        data = json.loads(request.body)
        status = data.get("status")
        user_profile = request.user.userprofile

        UserQuestionKnowledge.objects.update_or_create(
            user=user_profile,
            question_id=question_id,
            defaults={"knowledge_status": status},
        )
        return JsonResponse({"message": "Status updated successfully."})

    return JsonResponse({"error": "Invalid request."}, status=400)


@login_required
def calculate_user_progress(request, technology_id):

    user = request.user
    progress_instance, created = UserTechnologyProgress.objects.get_or_create(
        user=user,
        technology_id=technology_id,
    )

    modules = progress_instance.technology.modules.all()

    topics = Topic.objects.filter(module__in=modules)

    total_questions = Question.objects.filter(topic__in=topics).count()

    good_knowledge_count = UserQuestionKnowledge.objects.filter(
        user=user, question__topic__in=topics, knowledge_status="good"
    ).count()

    if total_questions > 0:
        progress_instance.progress_percentage = (
            good_knowledge_count / total_questions
        ) * 100
    else:
        progress_instance.progress_percentage = 0

    progress_instance.save()

    return JsonResponse(
        {
            "progress_percentage": progress_instance.progress_percentage,
            "message": "Progress updated successfully.",
        }
    )


def update_user_progress_view(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    user_profile = request.user.userprofile

    knowledge_status = request.POST.get("knowledge_status")

    user_question_knowledge, created = UserQuestionKnowledge.objects.get_or_create(
        user=user_profile, question=question
    )
    user_question_knowledge.knowledge_status = knowledge_status
    user_question_knowledge.save()

    try:
        progress_record = UserTechnologyProgress.objects.get(
            user=user_profile, technology=question.topic.module.technology
        )
        progress_record.calculate_progress()  # Recalculate progress
    except UserTechnologyProgress.DoesNotExist:
        UserTechnologyProgress.objects.create(
            user=user_profile,
            technology=question.topic.module.technology,
            progress_percentage=0,  # Initialize
        )

    return redirect("job_me:question_detail", question_id=question_id)
