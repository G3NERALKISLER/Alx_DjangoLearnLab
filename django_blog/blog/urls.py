from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.homeView, name='home'),
    path('posts/', views.PostListView, name='post-list'),
    path('posts/new/', views.PostCreateView, name='post-create'),
    path('posts/<int:pk>/',views. PostDetailView, name='post-detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView, name='post-update'),
    path('posts/<int:pk>/delete/',views.PostDeleteView, name='post-delete'),
    path('register/', views.register_view, name='register'),
    path('login/', views.Login_View, name='Login'),
     path("profile/", views.profile_view, name="profile"),
]
