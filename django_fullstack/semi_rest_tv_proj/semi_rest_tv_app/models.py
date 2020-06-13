from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=150)
    network = models.CharField(max_length=20)
    desc = models.TextField(default="null")
    release_date = models.DateField(auto_now=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
