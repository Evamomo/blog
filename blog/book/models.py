from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=128, unique=True)
    material = models.CharField(max_length=128)
    price = models.IntegerField()
    
    def __str__(self):
        return self.title
