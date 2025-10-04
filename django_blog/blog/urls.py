from django.urls import path
from . import views
from .views import PostByTagListView
app_name = 'blog'
urlpatterns = [
    path('', views.homeView, name='home'),
    path('post/', views.PostListView, name='post-list'),
    path('post/new/', views.PostCreateView, name='post-create'),
    path('post/<int:pk>/',views.PostDetailView, name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView, name='post-update'),
    path('post/<int:pk>/delete/',views.PostDeleteView, name='post-delete'),
    path('register/', views.register_view, name='register'),
    path('login/', views.Login_View, name='Login'),
    path("profile/", views.profile_view, name="profile"),
    path('post/<int:post_pk>/comments/', views.CommentListView.as_view(), name='comment_list'),
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('search/', views.search_posts, name='search_posts'),
    path('tags/<str:tag_name>/', PostByTagListView.as_view(), name='posts_by_tag'),
]
