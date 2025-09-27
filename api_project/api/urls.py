from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter
from . import views
from .views import BookList, BookViewSet, testBookmodel
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('api/books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('index/', views.testBookmodel, name="Bookmodel" )
]
