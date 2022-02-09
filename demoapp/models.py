from pyexpat import model
from django.db import models

# Create your models here.

# class Todo(models.Model):
#     task = models.CharField(max_length=30)
#     description = models.CharField(max_length=100)
class Todo(models.Model):
    textone = models.CharField(max_length=30)
    texttwo = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    upvotes = []
    answer = []
    answers = []
    date = models.DateTimeField()
   
