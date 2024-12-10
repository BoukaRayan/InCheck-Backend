from django.urls import re_path

from . import views

urlpatterns = [
    #re_path('signup', views.AdminSignupView.as_view()),
    re_path('login', views.AdminLoginView.as_view()),
]