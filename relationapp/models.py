from django.db import models

# Create your models here.
 
 
 
 
 
class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=20,unique=True)
    gender = models.CharField(max_length=50) 

    def __str__(self):
       return self.email


class Book(models.Model):
    title = models.CharField(max_length=50)
    auth = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='book')
    
    
    def __str__(self):
        return self.title