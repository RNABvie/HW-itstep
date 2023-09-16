from django.urls import path, reverse, reverse_lazy
from django_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path('registrations/', views.register, name="register"),
    path("login/", views.login_, name="login"),
]