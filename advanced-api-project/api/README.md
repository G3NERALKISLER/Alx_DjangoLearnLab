### Books API Query Features

- **Filtering**
  - `/books/?title=Harry%20Potter`
  - `/books/?author=J.K.%20Rowling`
  - `/books/?publication_year=2023`

- **Searching**
  - `/books/?search=Potter` → finds all books with "Potter" in the title or author’s name.

- **Ordering**
  - `/books/?ordering=title`
  - `/books/?ordering=-publication_year` (descending order by year)
### Running Tests
Run:
```bash
python manage.py test api
