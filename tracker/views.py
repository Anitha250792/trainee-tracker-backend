from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer
from django.views.generic import TemplateView


# ✅ API ViewSet (your existing code)
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by("-created_at")
    serializer_class = ProjectSerializer


# ✅ React Frontend View (new)
class ReactAppView(TemplateView):
    template_name = "index.html"
