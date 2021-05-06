from django.db import models

# Create your models here.

class contact_form(models.Model):
    Name = models.CharField(max_length=45)
    Email = models.CharField(max_length=45)
    Subject = models.CharField(max_length=100)
    Message = models.CharField(max_length=1000)