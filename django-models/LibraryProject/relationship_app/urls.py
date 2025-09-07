from django.urls import path
from . import views
from .views import list_books
from .views import LibraryDetailView
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('', list_books, name='home'),
    path('library/<int:pk>/',LibraryDetailView.as_view(), name='library_details'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
    path("register/", views.register, name="register"),

]