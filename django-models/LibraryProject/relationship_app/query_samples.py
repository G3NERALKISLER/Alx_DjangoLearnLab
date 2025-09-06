from relationship_app.models import Author,Book,Library

author = Author.objects.get(name="1984")
books_by_author = Book.objects.filter(author=author)

for book in books_by_author:
    print(book.title)


library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()

for book in books_in_library:
    print(book.title)

library = Library.objects.get(name="Central Library")
librarian = library.librarian  # thanks to OneToOneField related_name
print(librarian.name)
