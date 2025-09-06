from django.urls import path
from . import views

urlpatterns=[
    path('', views.list_book, name='list_book'),
    path('library_details', views.display_details, name='library_details')
]