from turtle import title
from django.db import models


# Create your models here.
class TodoApp(models.Model):
    # fields
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
