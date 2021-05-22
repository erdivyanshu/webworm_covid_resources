from django.db import models

# Create your models here.
# contact us form

class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     email= models.CharField(max_length=100)
     need= models.CharField(max_length=255)
     content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
          return 'Need of ' + self.need

class Feedback(models.Model):
     sno= models.AutoField(primary_key=True)
     email= models.CharField(max_length=100)
     text= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
          return self.email

class Resources(models.Model):
     CATEGORY = (('Vaccine','Vaccine'), ('General-Bed','General-Bed'), ('Oxygen-Bed','Oxygen-Bed'),('Bed With-Ventilator','Bed With-Ventilator'))
     sno= models.AutoField(primary_key=True)
     Hname= models.CharField(max_length=200)
     category= models.CharField(max_length=200, null=True, choices=CATEGORY)
     available= models.IntegerField(null=True)
     #for contact details
     add = models.TextField()
     contact = models.TextField()

     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
          return self.Hname

