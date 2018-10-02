from django.urls import path, include
from . import views

urlpatterns = [
    path('new', views.create_post, name='create_post' ),
    #path('', views.list_post, name='feed' ),
] 