from django.urls import path
from . import views

urlpatterns = [
    path("", views.talk, name="blank"),
    path("test/", views.index, name = "home")
]