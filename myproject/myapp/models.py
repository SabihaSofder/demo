from django.db import models

# Create your models here.
class contact(models.Model):
  full_name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  phone_number = models.CharField(max_length=20)
  subject = models.CharField(max_length=255)
  message = models.CharField(max_length=300)
