from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view as get_schema_view_rest


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', include('loginas.urls')),
    path('api-auth/', include('rest_framework.urls'), name='rest-auth'),
    path('openapi/', get_schema_view_rest(), name='openapi-schema'),
    path('ht/', include('health_check.urls')),
    path('', include('user.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
                   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
