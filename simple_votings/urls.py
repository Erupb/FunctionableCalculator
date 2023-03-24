"""simple_votings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path

from main import views
from django.contrib.auth import views as auth_views

from main.views import get_menu_context, MyLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing'),
    path('main/', views.index_page, name='index'),
    path('', views.index_page, name='index'),
    path('elementary_mathematics/', views.elementary_mathematics, name='elementary_mathematics'),
    path('trigonometry/', views.trigonometry, name='trigonometry'),
    path('graphic/', views.graphic_page, name='graphic'),
    path('equation/', views.equation_page, name='equation'),
    path('currency/', views.currency, name='currency'),
    path('stereometry/', views.stereometry, name='stereometry'),
    path('antiderivative/', views.antiderivative_page, name='antiderivative'),
    path('login/', MyLoginView.as_view()),
    path('login/', auth_views.LoginView.as_view(
        extra_context={
            'menu': get_menu_context(),
            'pagename': 'Авторизация',
        }), name='login'),
    path('integral/', views.integral, name='integral'),
    path('factorial/', views.factorial, name='factorial'),
    path('login/', auth_views.LoginView.as_view(
        extra_context={
            'menu': get_menu_context(),
            'pagename': 'Авторизация',
        }), name='login'),
    path('reg/', views.registration_user, name='registration',),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('factorial/', views.factorial, name='factorial'),
    path('api/db/', views.save_data_to_db, name='db'),
    path('number_system/', views.number_system, name='number_system'),
    path('factorial/', views.factorial, name='factorial'),
]
