from django.db import models

# Create your models here.

class ClientsMessages(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    