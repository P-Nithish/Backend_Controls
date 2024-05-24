# controlsApp/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from controlsApp.views import ControlViewSet, ControlSetViewSet, ControlHierarchyViewSet

router = DefaultRouter()
router.register(r'controls', ControlViewSet)
router.register(r'controlsets', ControlSetViewSet)
router.register(r'controlhierarchies', ControlHierarchyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
