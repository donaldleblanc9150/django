from django.db import models

class PlayerManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData["first_name"]) < 2:
            errors["first_name"] = "Player first name should be at least 2 characters"
        if len(postData["last_name"]) < 2:
            errors["last_name"] = "Player last name should be at least 2 characters"
        if len(postData["team"]) < 3:
            errors["team"] = "Team name should be at least 3 characters"
        return errors

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    team = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PlayerManager()
