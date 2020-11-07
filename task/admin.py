from django.contrib import admin
from .models import (
	TaskCategory,
	Status,
	Task,
	ChatTask,
	ChatMessage,
	Sprint,
	Priority
)

admin.site.register(TaskCategory)
admin.site.register(Status)
admin.site.register(Task)
admin.site.register(ChatTask)
admin.site.register(ChatMessage)
admin.site.register(Sprint)
admin.site.register(Priority)