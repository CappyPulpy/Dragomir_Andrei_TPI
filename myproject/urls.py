"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth.views import LogoutView
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('login', login_view, name='login'),
    path('signup', signup_view, name='signup'),
    path('landing', landing_view, name='landing'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('update_balance', update_balance_view, name='update_balance')
]
