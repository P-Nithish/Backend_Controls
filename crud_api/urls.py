from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from controlsApp.views import ControlViewSet, ControlSetViewSet, ControlHierarchyViewSet

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Controls API",
        default_version='v1',
        description="API documentation for the Controls application",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('controlsApp.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
