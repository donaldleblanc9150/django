from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=255)


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="publishers")

    created_at = models.DateTimeField(auto_now_add=255)
    updated_at = models.DateTimeField(auto_now=255)
