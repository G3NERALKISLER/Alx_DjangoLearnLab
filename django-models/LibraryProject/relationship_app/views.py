from django.shortcuts import render
from .models import Book
from .models import Library
# Create your views here.
def list_book(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html',{'books' : books})

def display_details(request):
    library = Library.objects.all()
    return render(request, 'relationship_app/library_detail.html', {'library': library})