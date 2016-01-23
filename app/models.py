from django.db import models


class Breed(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Dog(models.Model):
    name = models.CharField(max_length=64, unique=True)
    breed = models.ForeignKey(Breed, on_delete=models.PROTECT)
    
