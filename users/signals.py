from django.contrib.auth.models import User
from .models import UserProfile
from django.dispatch import receiver
from django.db.models.signals import post_save
from allauth.socialaccount.models import SocialAccount


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    try:
        instance.userprofile.save()
    except UserProfile.DoesNotExist:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=SocialAccount)
def create_social_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance.user)
