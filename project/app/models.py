from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='author_book',null=False,blank=False)

    def __str__(self):
        return self.name