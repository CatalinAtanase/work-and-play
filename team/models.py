from django.db import models
from accounts.models import User


class Team(models.Model):
    name = models.CharField(
        max_length=100,
    )
    points = models.IntegerField()
    password = models.CharField(max_length=20)
    hint = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.name


class TeamPoints(models.Model):
    team = models.OneToOneField(
        Team,
        on_delete=models.CASCADE
    )
    points = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.team.name} points at {self.date}."

    class Meta:
        verbose_name = "Team Points"
        verbose_name_plural = "Team Points"
