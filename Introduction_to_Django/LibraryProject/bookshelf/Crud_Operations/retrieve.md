# Retrieve Operation

```python
book = Book.objects.get(title="1984")
book.title, book.author, book.description, book.published_date
# Output: ('1984', 'George Orwell', 'A dystopian social science fiction novel.', datetime.date(1949, 6, 8))
