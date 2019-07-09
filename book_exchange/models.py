from django.db import models

# Create your models here.

BOOK_STATUS_OPTIONS = (
    ("sale", "sale"),
    ("giveaway", "giveaway")
)

class Category(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length = 30)

    def __str__(self):
        return self.title


class Book(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length = 100)
    category = models.ForeignKey(Category, related_name = "category", on_delete = models.CASCADE)
    status =  models.CharField(choices=BOOK_STATUS_OPTIONS, default='sale', max_length=100)# (sale, givaway)
    availability = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='book', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Contact_info(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    phone  = models.CharField(max_length=25)
    email =  models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Offer(models.Model):
    sender = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        string = "from ",self.sender.name, " to ", self.book.owner.name
        return string
