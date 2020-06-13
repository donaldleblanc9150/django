from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    # creating a new instance of the ManyToManyField class
    books = models.ManyToManyField(
        # connecting the Book class via the "books" attribute
        # every "book" will be an instance of the Book class
        Book,
        # creating a "hidden field" on each Book object
        #that allows us to reference the Book's authors
        # ex: Java.authors.all() - Java being a book in Books class with an author
        related_name="authors")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)