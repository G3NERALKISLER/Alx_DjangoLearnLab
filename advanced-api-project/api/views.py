from django_filters import rest_framework
from rest_framework import generics,permissions
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # anyone can view
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

 
    filterset_fields = ["title", "author", "publication_year"]

   
    search_fields = ["title", "author__name"]  

  
    ordering_fields = ["title", "publication_year"]
    ordering = ["title"]  



class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# 3. Create a new book
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # must be logged in


# 4. Update an existing book
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # must be logged in


# 5. Delete a book
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # must be logged in

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True
        return request.user and request.user.is_staff

class AuthorCreateView(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer