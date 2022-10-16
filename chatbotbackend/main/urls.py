from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.index, name = "home"),
    path("email_form/", views.email_form, name="email_form"),
    path("send/", views.send, name="send_email")
]