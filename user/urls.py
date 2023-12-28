from django.contrib import admin
from django.urls import path
from user import views
app_name = "user"
urlpatterns = [

    path('register/', views.RegisterForm.as_view(),name="register"),
    path('login/', views.LoginForm.as_view(),name="login"),
]
