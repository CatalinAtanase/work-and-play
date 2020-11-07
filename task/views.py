from django.shortcuts import render
from rest_framework import viewsets, exceptions, status
from rest_framework.generics import RetrieveAPIView
from .models import (
    TaskCategory,
    Status,
    Task,
    ChatTask,
    ChatMessage,
    Sprint,
)
from .serializers import (
    SprintWithTasksSerializer, TaskCategorySerializer,
    StatusSerializer, TaskDetailsSerializer,
    TaskSerializer,
    ChatTaskSerializer,
    ChatMessageSerializer,
    SprintSerializer,
)


class TaskCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = TaskCategorySerializer
    queryset = TaskCategory.objects.all()
    # authentication_classes = []
    # permission_classes = []


class StatusViewSet(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    # authentication_classes = []
    # permission_classes = []


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(user=user)

        return queryset


class TaskDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = TaskDetailsSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(user=user)

        return queryset
    # authentication_classes = []
    # permission_classes = []


class ChatTaskViewSet(viewsets.ModelViewSet):
    serializer_class = ChatTaskSerializer
    queryset = ChatTask.objects.all()
    # authentication_classes = []
    # permission_classes = []


class ChatMessageViewSet(viewsets.ModelViewSet):
    serializer_class = ChatMessageSerializer
    queryset = ChatMessage.objects.all()
    # authentication_classes = []
    # permission_classes = []


class SprintViewSet(viewsets.ModelViewSet):
    serializer_class = SprintSerializer
    queryset = Sprint.objects.all()


class SprintDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = SprintWithTasksSerializer
    queryset = Sprint.objects.all()



class SprintLatest(viewsets.ModelViewSet):
    queryset = Sprint.objects.order_by('-id')[:1]
    serializer_class = SprintSerializer


