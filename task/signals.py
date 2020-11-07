from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Task, ChatTask

@receiver(post_save, sender=Task)
def password_reset_token_created(sender, instance, created, *args, **kwargs):
    if created:
        ChatTask.objects.create(task=instance)