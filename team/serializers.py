from accounts.serializers import UserSerializer
from rest_framework import serializers
from .models import (
    Team,
    TeamPoints,
)


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            "id",
            "name",
            "points",
            "hint",
            "password",
        )


class TeamDetailsSerializer(serializers.ModelSerializer):
    team_members = UserSerializer(many=True)

    class Meta:
        model = Team
        fields = (
            "id",
            "name",
            "points",
            "hint",
            "password",
			"team_members",
        )


class TeamPointsSerializer(serializers.ModelSerializer):
    # team = TeamMemberSerializer(many=True)

    class Meta:
        model = TeamPoints
        fields = (
            "id",
            "team",
            "points",
			"date",
        )


