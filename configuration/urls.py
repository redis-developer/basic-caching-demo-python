from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('repos/', include('repository.urls')),
    path('admin/', admin.site.urls),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
]
