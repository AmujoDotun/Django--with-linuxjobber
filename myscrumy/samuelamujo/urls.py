
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views 
from samuelamujoscrumy import views
urlpatterns = [
path('', views.index, name = 'index'),
]