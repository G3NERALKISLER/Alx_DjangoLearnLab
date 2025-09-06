from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
     path('books/suggest/', views.suggest_book, name='suggest_book'),
]
 