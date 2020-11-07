from django.db import models
from accounts.models import User
from colorfield.fields import ColorField


class TaskCategory(models.Model):
    name = models.CharField(
        max_length=200,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Task categories"


class Status(models.Model):
    status = models.CharField(
        max_length=200,
    )
    color = ColorField()

    def __str__(self):
        return self.status

    class Meta:
        verbose_name_plural = "Status"


class Priority(models.Model):
    priority = models.CharField(
        max_length=200,
    )
    color = ColorField()

    def __str__(self):
        return self.priority

    class Meta:
        verbose_name_plural = "Priorities"


class Sprint(models.Model):
    name = models.CharField(
        max_length=200
    )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        # related_name="user_tasks",
        blank=True,
        null=True
    )
    sprint = models.ForeignKey(
        Sprint,
        on_delete=models.CASCADE,
        related_name="sprint_tasks",
        null=True,
        blank=True
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    name = models.CharField(
        max_length=200,
    )
    description = models.TextField()
    category = models.ForeignKey(
        TaskCategory,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    points = models.IntegerField()
    deadline = models.DateTimeField()
    priority = models.ForeignKey(
        Priority,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.name} - by {self.user.username}"


class ChatTask(models.Model):
    task = models.OneToOneField(
        Task,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task.name} chat"


class ChatMessage(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="chat_messages",
        blank=True,
        null=True
    )
    chat = models.OneToOneField(
        ChatTask,
        on_delete=models.CASCADE,
        related_name="chat_messages"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s message on {self.chat}"
