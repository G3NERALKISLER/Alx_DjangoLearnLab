from django.urls import path
from . import views

urlpatterns=[
    path('', views.list_book, name='list_book'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_details')
]