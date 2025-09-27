from rest_framework import generics,permissions
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.permissions import BasePermission
class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # anyone can view


# 2. Retrieve a single book by ID
class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# 3. Create a new book
class BookCreateAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # must be logged in


# 4. Update an existing book
class BookUpdateAPIView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # must be logged in


# 5. Delete a book
class BookDeleteAPIView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # must be logged in

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True
        return request.user and request.user.is_staff

class AuthorCreateAPIView(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer