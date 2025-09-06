from django import forms
from .models import BookSuggestion

class BookSuggestionForm(forms.ModelForm):
    class Meta:
        model = BookSuggestion
        fields = ['title', 'author', 'publication_year', 'status']
