from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('blogs', views.blogs),
    path('blog/<int:blog_id>', views.blog),
    path('contact', views.contact),
]
