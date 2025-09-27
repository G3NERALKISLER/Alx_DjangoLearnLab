from django.urls import path
from .views import (
    BookListAPIView,
    BookDetailAPIView,
    BookCreateAPIView,
    BookUpdateAPIView,
    BookDeleteAPIView,
)

urlpatterns = [
   
    path("books/", BookDetailAPIView.as_view(), name="book-detail"),
    path("books/create/", BookCreateAPIView.as_view(), name="book-create"),
    path("books/update/", BookUpdateAPIView.as_view(), name="book-update"),
    path("books/delete/", BookDeleteAPIView.as_view(), name="book-delete"),
]
