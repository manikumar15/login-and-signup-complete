from django.db import models

class Register(models.Model):
    
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Enquiry(models.Model):
    
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=30)
    phone=models.CharField(max_length=50)
    jobtype=models.CharField(max_length=30)
 

    
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class News(models.Model):
    Email = models.EmailField()

    def __str__(self):
        return self.Email