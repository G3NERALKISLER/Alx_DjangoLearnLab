from django.shortcuts import render
from .models import Book,Library
# Create your views here.
def list_book(request):
    books = Book.objects.all()
    return render(request, 'list_books.html',{'books' : books})

def display_details(request):
    library = Library.objects.all()
    return render(request, 'library_detail.html', {'library': library})