from django.db import models

# Create your models here.

class Client(models.Model):
    account_type = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    active = models.BooleanField(default=True)


class Address(models.Model):
    street = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=2)
    appt_num = models.IntegerField()


class Video(models.Model):
    title = models.CharField(max_length=100)
    in_stock = models.IntegerField()
    rating = models.CharField(max_length=1)


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_init = models.CharField(max_length=1)
    age = models.IntegerField()

class Store(models.Model):
    name = models.CharField(max_length=100)
    number_of_employees = models.IntegerField()
    rating = models.FloatField(max_length=3)
    owner = models.IntegerField()