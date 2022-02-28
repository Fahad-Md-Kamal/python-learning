from django.db import models

class Book(models.Model):
    name = models.CharField("Book Name", max_length=200)
    author = models.CharField("Author Name", max_length=200)
    isbn = models.CharField("Book ISBN", max_length=200)

class Shop(models.Model):
    name = models.IntegerField()
    address = models.TextField()
