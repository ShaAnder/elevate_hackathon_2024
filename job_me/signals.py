from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import UserProfile
from .models import UserQuestionKnowledge, UserTechnologyProgress, Technology


@receiver(post_save, sender=UserProfile)
def create_user_technology_progress(sender, instance, created, **kwargs):
    if created:
        # Get all technologies and create a progress entry for each
        technologies = Technology.objects.all()
        for tech in technologies:
            UserTechnologyProgress.objects.create(user=instance, technology=tech)


@receiver(post_save, sender=UserQuestionKnowledge)
def update_user_progress(sender, instance, **kwargs):
    try:
        # Get the user's progress record for the technology
        progress_record = UserTechnologyProgress.objects.get(
            user=instance.user,
            technology=instance.question.topic.module.technology,
        )
        progress_record.calculate_progress()  # Recalculate progress based on new knowledge status
    except UserTechnologyProgress.DoesNotExist:
        UserTechnologyProgress.objects.create(
            user=instance.user,
            technology=instance.question.topic.module.technology,
            progress_percentage=0,  # Initialize with 0
        )
