from accounts.serializers import UserSerializer
from rest_framework import serializers
from .models import (
    Priority, TaskCategory,
    Status,
    Task,
    ChatTask,
    ChatMessage,
    Sprint,
)


class TaskCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskCategory
        fields = (
            "id",
            "name",
        )


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = (
            "id",
            "status",
            "color",
        )


class ChatTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatTask
        fields = (
            "id",
            "created_at",
        )


class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = (
            "id",
            "priority",
            "color",
        )


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "id",
            "name",
            "description",
            "points",
            "deadline",
        )


class TaskDetailsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    status = StatusSerializer()
    category = TaskCategorySerializer()
    priority = PrioritySerializer()

    class Meta:
        model = Task
        fields = (
            "id",
            "name",
            "description",
            "points",
            "user",
            "deadline",
            "status",
            "category",
            "chattask",
            "priority",
        )


class ChatMessageSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    chat = ChatTaskSerializer()

    class Meta:
        model = ChatMessage
        fields = (
            "id",
            "user",
            "chat",
            "content",
            "created_at",
            "updated_at",
        )


class SprintWithTasksSerializer(serializers.ModelSerializer):
    sprint_tasks = TaskDetailsSerializer(many=True)

    class Meta:
        model = Sprint
        fields = (
            "id",
            "name",
            "created_at",
            "sprint_tasks",
        )


class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = (
            "id",
            "name",
            "created_at",
        )
