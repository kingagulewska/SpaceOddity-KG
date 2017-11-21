from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Planet(models.Model):
    name = models.CharField(max_length=50)
    main_photo = models.CharField(max_length=100)
    small_photo = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    description_long = models.CharField(max_length=1000)


    def __str__(self):
        return self.name


class House(models.Model):
    price = models.IntegerField()
    planet = models.ForeignKey(Planet, related_name='houses')
    owner = models.ForeignKey(User, related_name='houses', blank=True, null=True)
    name = models.CharField(max_length=50)
    house_photo = models.CharField(max_length=100)

    def __str__(self):
        owner = self.owner if self.owner else 'noone'
        return "House #{} owned by {} [{}$]".format(self.id, owner, self.price)



