from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('blogs', views.blogs),
    path('contact', views.contact),
]
