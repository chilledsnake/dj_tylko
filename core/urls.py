from django.contrib import admin
from django.urls import include, path

from api.urls import urlpatterns as api_urlpatterns
from core.utils.openapi_schema import urlpatterns as openapi_schema_urlpatterns

urlpatterns = [path("admin/", admin.site.urls), path("api/", include(api_urlpatterns))]

urlpatterns += openapi_schema_urlpatterns
