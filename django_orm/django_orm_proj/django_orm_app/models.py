from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    fav_number = models.IntegerField()
    motto = models.TextField()

    # albums = is being created below

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Album(models.Model):
    artist = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    release_date = models.DateField()
    genre = models.CharField(max_length=20)
    owner = models.ForeignKey(
        User, related_name="albums", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
