from django.db import models
from django.contrib.auth.models import User
from book_exchange.models import Book
# Create your models here.

class ContactInfo(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=25)
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
    location = models.TextField()
    note = models.TextField()

class Offer(models.Model):
    sender = models.ForeignKey(User, related_name = 'sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Book, related_name = 'receiver', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
