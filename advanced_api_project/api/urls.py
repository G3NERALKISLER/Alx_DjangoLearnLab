from django.urls import path
from . import views
from .views import BookListCreateAPIView, AuthorCreateAPIView

urlpatterns = [
    path("books/", views.BookListCreateAPIView.as_view(), name="book_list_create"),
    path("author/", views.AuthorCreateAPIView.as_view(), name="Authorcreate"),
]
