# bookshelf/forms.py
from django import forms
from .models import Book

# For creating/editing books safely


# For searching books safely
class SearchForm(forms.Form):
    q = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Search books..."}),
    )
