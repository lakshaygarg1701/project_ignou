from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView
from django.urls import path
from . import views


urlpatterns=[
	path('', include('django.contrib.auth.urls')),
	path('signup/', views.FacSignup, name='signup'),
]