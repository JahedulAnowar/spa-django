from django.db import models


class Breed(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Breed(id=%d,name='%s')" % (self.id, self.name)


class Dog(models.Model):
    name = models.CharField(max_length=64, unique=True)
    breed = models.ForeignKey(Breed, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return "Dog(id=%d,name='%s')" % (self.id, self.name)

