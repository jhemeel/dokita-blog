from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/', views.blogs, name='blogs'),
    path('post/', views.post, name='post'),
]
