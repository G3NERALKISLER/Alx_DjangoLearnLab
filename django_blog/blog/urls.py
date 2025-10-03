from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.homeView, name='home'),
    path('post/', views.PostListView, name='post-list'),
    path('post/new/', views.PostCreateView, name='post-create'),
    path('post/<int:pk>/',views.PostDetailView, name='post-detail'),
    path('post/<int:pk>/edit/', views.PostUpdateView, name='post-update'),
    path('post/<int:pk>/delete/',views.PostDeleteView, name='post-delete'),
    path('register/', views.register_view, name='register'),
    path('login/', views.Login_View, name='Login'),
     path("profile/", views.profile_view, name="profile"),
]
