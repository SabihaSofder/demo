from django.db import models



class contactUs(models.Model) :
    contactFullName = models.CharField(max_length=50)
    contactEmail = models.CharField(max_length=50)
    contactPhoneNumber = models.IntegerField()
    contactSubject = models.CharField(max_length=50)
    contactMessage = models.TextField()
