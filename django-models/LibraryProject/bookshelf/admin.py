
from django.contrib import admin
from .models import Book  # import your model
from .models import  BookSuggestion
# Register your model

@admin.register(Book) 

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    search_fields = ("title", "author,")
    list_filter = ("publication_year",)
 
    ordering = ("-publication_year",)
@admin.register(BookSuggestion)

class BookSuggestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year', 'status')
    actions = ['approve_suggestions', 'reject_suggestions']

    def approve_suggestions(self, request, queryset):
        added_count = 0
        for suggestion in queryset:
            # Only add if it hasn’t been approved before
            if suggestion.status != "approved":
                # Create the actual Book
                Book.objects.create(
                    title=suggestion.title,
                    author=suggestion.author,
                    publication_year=suggestion.publication_year
                )
                # Mark suggestion as approved
                suggestion.status = "approved"
                suggestion.save()
                added_count += 1

        # Show feedback in Django admin
        self.message_user(request, f"{added_count} suggestion(s) approved and added to the library.")

    approve_suggestions.short_description = "Approve selected suggestions (Add to Books)"

    def reject_suggestions(self, request, queryset):
        updated = queryset.update(status="rejected")
        self.message_user(request, f"{updated} suggestion(s) rejected.")

    reject_suggestions.short_description = "Reject selected suggestions"