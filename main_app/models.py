from django.db import models
from django.urls import reverse

# Create your models here.

class Icon(models.Model):
    sneaker = models.TextField()
    why = models.TextField()
    sneaker_type = models.TextField()
    description = models.TextField()
    debut_year = models.IntegerField()

class User_Sneaker(models.Model):
    sneaker = models.CharField(max_length=100)
    sneaker_type = models.CharField(max_length=100)
    description = models.TextField()
    debut_year = models.IntegerField() 
    price = models.CharField(max_length=100)

    # changes the instance method
    def __str__(self):
        return f'{self.sneaker} ({self.id})'

    # changes the redirect after the add sneaker form is completed
    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'user_sneaker_id': self.id})