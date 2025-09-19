from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "assigned_to", "priority", "status", "due_date", "created_at")
    list_filter = ("priority", "status")
    search_fields = ("title", "assigned_to")
