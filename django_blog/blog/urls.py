from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.homeView, name='home'),
    path('posts/', views.PostView, name='posts'),
    path('register/', views.register_view, name='register'),
    path('login/', views.Login_View, name='Login'),
     path("profile/", views.profile_view, name="profile"),
]
