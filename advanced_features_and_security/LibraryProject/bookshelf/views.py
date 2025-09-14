from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book
from  django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django import forms
@login_required
# Create your views here.
def book_list(request): 
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html',{'books' : books})
@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
    # Logic to create a book
    return HttpResponse("Book created")

@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Logic to edit book
    return HttpResponse(f"Book {book.title} edited")

@permission_required("bookshelf.can_delete", raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return HttpResponse(f"Book {book.title} deleted")

class SearchForm(forms.Form):
    q = forms.CharField(max_length=100)

def search_books(request):
    form = SearchForm(request.GET or None)
    results = []
    if form.is_valid():
        query = form.cleaned_data["q"]
        results = Book.objects.filter(title__icontains=query)  # ORM prevents SQL injection
    return render(request, "bookshelf/search.html", {"form": form, "results": results})