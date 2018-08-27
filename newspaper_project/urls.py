from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

API_TITLE = 'API'
API_DESCRIPTION = 'A Web API for creating and editing articles.'
schema_view = get_swagger_view(title=API_TITLE)

urlpatterns = [
    path('', include('pages.urls')),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('articles.api.urls')),
    path('api/', schema_view),
]
