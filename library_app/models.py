from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
   # quantity = models.IntegerField(max_length=10)git
    available = models.BooleanField(default=True)


class BorrowRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE) 
    request_date = models.DateField()
    is_approved = models.BooleanField()
