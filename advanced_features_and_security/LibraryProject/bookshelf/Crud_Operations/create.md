# Create Operation

```python
from books.models import Book
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    description="A dystopian social science fiction novel.",
    published_date="1949-06-08"
)
book
# Output: <Book: 1984>
