from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('repos/', include('repository.urls')),
    path('admin/', admin.site.urls),
]
