
from django.contrib import admin
from .models import Book  # import your model

# Register your model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns shown in admin
