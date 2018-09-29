from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list_post, name='feed' ),
] 