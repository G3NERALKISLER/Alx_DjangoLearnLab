from django.shortcuts import render
from .models import Book

from django.contrib.auth.decorators import login_required
@login_required
# Create your views here.
def book_list(request): 
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html',{'books' : books})
