from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tracker.views import ProjectViewSet, ReactAppView

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),   # 👈 all API endpoints now under /api/
    path("", ReactAppView.as_view(), name="react-app"),
]
