from django.urls import path
from .views import list_book
from .views import LibraryDetailView

urlpatterns=[
    path('', list_book, name='list_book'),
    path('library/<int:pk>/',LibraryDetailView.as_view(), name='library_details')
]