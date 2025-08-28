# Delete Operation

```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
# Output: (1, {'books.Book': 1})
# After deletion, no books remain: <QuerySet []>
