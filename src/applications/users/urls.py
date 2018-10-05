from django.urls import path, include
from . import views


urlpatterns = [
    path('login/', views.auth_view, name='login' ),
    path('logout/', views.logout_view, name='logout' ),
    path('signup/', views.signup_view, name='signup' ),
    path('me/profile/', views.update_profile, name='update_profile' ),
    path('<str:username>/', views.UserDetailView.as_view(), name='detail'),
] 