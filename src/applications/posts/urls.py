from django.urls import path, include
from . import views

urlpatterns = [
    path('posts/new/', views.CreatePostView.as_view(), name='create_post' ),
    path('posts/<int:pk>', views.PostsDetailView.as_view(), name='detail' ),
    path('', views.PostsFeedView.as_view(), name='feed' ),
    
] 