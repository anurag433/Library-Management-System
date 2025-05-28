from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    edition = models.IntegerField()
    available = models.BooleanField(default=True)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True , null= True)

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    join_date = models.DateField(auto_now_add=True)

class IssuedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    issued_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()