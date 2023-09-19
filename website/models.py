from django.db import models

# Create your models here.
class GeneralInformation(models.Model):
    name = models.CharField(max_length=100)
    student_at = models.CharField(max_length=200)
    connections = models.CharField(max_length=10)
    profile_language = models.CharField(max_length=100)
    public_profile_url = models.URLField(max_length=200)
    def __str__(self):
        return self.name
    
class Education(models.Model):
    user=models.ForeignKey(GeneralInformation,on_delete=models.CASCADE)
    qualification = models.CharField(max_length=100)
    college_name = models.CharField(max_length=200)
    branch = models.CharField(max_length=100)
    time_period = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class Address(models.Model):
    user=models.ForeignKey(GeneralInformation,on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class LicensesCertifications(models.Model):
    user=models.ForeignKey(GeneralInformation,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    organisation = models.CharField(max_length=200)

class Person(models.Model):
    user=models.ForeignKey(GeneralInformation,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Skills(models.Model):
    user=models.ForeignKey(GeneralInformation,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    assesment = models.CharField(max_length=200)

class Resources(models.Model):
    user=models.ForeignKey(GeneralInformation,on_delete=models.CASCADE)
    creator_mode = models.CharField(max_length=100)
    creator_description = models.TextField()
    my_network = models.TextField()
