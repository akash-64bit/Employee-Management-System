from django.db import models

# Create your models here.

class Employees(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=100)
    address = models.TextField()
    phone = models.IntegerField(max_length=10)

    def __str__(self):
        return self.name