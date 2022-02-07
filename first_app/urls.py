"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from first_app import views

app_name = "first_app"

urlpatterns = [
    path('',views.index,name="index"),
    path('data/',views.data_index,name="data_index"),
    path('user/',views.user_index,name="user_index"),
    path('basicform/',views.form_name_view,name="form_name"),
    path('signup/',views.signup_user,name="signup_user"),
    path('relative_url/',views.relative_url,name="relative_url"),
    path('other_page/',views.other_page,name="other_page"),
]
