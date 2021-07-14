from django.db import models

# Create your models here.

class Customer(models.Model):
    name= models.CharField(max_length=100)
    number = models.IntegerField(max_length=10)
    email = models.EmailField()
    balance = models.IntegerField()

    def __str__(self):
        return self.name


class Transfer(models.Model):
     sender_name = models.CharField(max_length=400)
     amount = models.IntegerField()
     receiver_name = models.CharField(max_length=50)

     def __str__(self):
         return self.sender_name