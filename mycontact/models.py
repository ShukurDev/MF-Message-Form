from django.db import models
from django.urls import reverse

from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = PhoneNumberField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('home')

