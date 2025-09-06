from django.urls import path
from .views import list_books
from .views import LibraryDetailView

urlpatterns=[
    path('', list_books, name='list_book'),
    path('library/<int:pk>/',LibraryDetailView.as_view(), name='library_details')
]