from django.shortcuts import render,  redirect
from .models import Book
from .forms import BookSuggestionForm
from .models import Book, BookSuggestion
from django.contrib.auth.decorators import login_required
@login_required
# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html',{'books' : books})
def suggest_book(request):
    if request.method == 'POST':
        form = BookSuggestionForm(request.POST)
        if form.is_valid():
            suggestion = form.save(commit=False)
            suggestion.user = request.user
            suggestion.status = 'pending'  # ensure all suggestions are pending
            suggestion.save()
            return redirect('book_list')  # or any page you want
    else:
        form = BookSuggestionForm()
    return render(request, 'bookshelf/suggest_book.html', {'form': form})


# Optional: Admin view to approve/reject suggestions
@login_required
def review_suggestions(request):
    if not request.user.is_staff:
        return redirect('book_list')  # only admin/staff can review

    suggestions = BookSuggestion.objects.filter(status='pending')
    return render(request, 'bookshelf/review_suggestions.html', {'suggestions': suggestions})