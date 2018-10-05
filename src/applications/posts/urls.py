from django.urls import path, include
from . import views

urlpatterns = [
    path('posts/new', views.create_post, name='create_post' ),
    path('', views.PostsFeedView.as_view(), name='feed' ),
] 