from django.contrib import admin
from .models import (
    Team,
    TeamPoints,
)

admin.site.register(Team)
admin.site.register(TeamPoints)
