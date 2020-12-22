from django.urls import path

from . import views

urlpatterns = [
  path('<str:repository_name>', views.GetRepositoriesView.as_view()),
]
