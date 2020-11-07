
from django.shortcuts import render
from .models import (
    Team,
    TeamPoints,
)
from .serializers import (
    TeamDetailsSerializer, 
    TeamSerializer,
    TeamPointsSerializer,
)
from rest_framework import viewsets


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class TeamDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = TeamDetailsSerializer
    queryset = Team.objects.all()



class TeamPointsViewSet(viewsets.ModelViewSet):
    serializer_class = TeamPointsSerializer
    queryset = TeamPoints.objects.all()
    authentication_classes = []
    permission_classes = []
