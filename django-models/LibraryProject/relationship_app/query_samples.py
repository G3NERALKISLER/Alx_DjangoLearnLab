from relationship_app.models import Author,Book,Library
author_name = "1984"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

for book in books_by_author:
    print(book.title)

library_name = "Main Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

for book in books_in_library:
    print(book.title)

library = Library.objects.get(name=library_name)
librarian = library.librarian  # thanks to OneToOneField related_name
print(librarian.name)
