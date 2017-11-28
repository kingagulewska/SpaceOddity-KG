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
    house_desc_short = models.CharField(max_length=150)
    house_desc_long = models.CharField(max_length=5000)
    size = models.IntegerField()
    bedroom_no = models.IntegerField()

    def __str__(self):
        owner = self.owner if self.owner else 'noone'
        return "House #{} owned by {} [{}$]".format(self.id, owner, self.price)

'''
class Buyer(models.Model):
    house = models.ForeignKey(House)
    planet = models.ForeignKey(Planet)
    owner = models.ForeignKey(User, blank=True, null=True)
    title = models.CharField(max_length=5)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_add = models.CharField(max_length=50)
    phone_numb = models.CharField(max_length=10)
    extra_message = models.CharField(max_length=500)

    def __str__(self):
        owner = self.owner if self.owner else 'noone'
        return "You are interested in house {} owned by {}. Details has been sent to Your email address: {}".format(
            self.house, owner, self.email_add)
'''