# Django Security Practices

- DEBUG set to False in production
- CSRF & Session cookies secured with HTTPS
- XSS, Clickjacking, and MIME sniffing protection enabled
- All forms include {% csrf_token %}
- ORM used instead of raw queries to prevent SQL injection
- Content Security Policy added to restrict sources
