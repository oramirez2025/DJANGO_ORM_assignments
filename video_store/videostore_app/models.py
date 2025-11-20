from django.db import models
from django.core import validators as v

class Client(models.Model):
    # recall: Adam said not null & unique <=> primary key.
    # or we could use primary_key=True
    # ALSO: can't have negative ids...
    id = models.PositiveIntegerField(primary_key=True)
    account_type = models.CharField(null=False, default="Regular")
    # required so we can contact them
    email = models.EmailField(null=False)
    # it's either they're active or not
    # I'll give them a default value of true just because they start off as active once they've created an account
    active = models.BooleanField(null=False, default=True)


class Video(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    # all videos must have a title; otherwise, how would we distinguish between videos lol
    title = models.CharField(null=False)
    # Can't have negative stock...
    in_stock = models.PositiveIntegerField(null=False)
    # it's okay to have null because what if a movie hasn't received a rating yet
    rating = models.CharField(null=True) 

# this one's pretty easy just because everyone has a first name and last name (other than Ye) and age
class Person(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    first_name = models.CharField(null=False)
    last_name = models.CharField(null=False)
    # I think they meant middle name by this...
    middle_name = models.CharField(null=True)
    age = models.PositiveIntegerField(null=False)


class Address(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    street = models.CharField()
    zipcode = models.IntegerField(validators=[v.MinValueValidator(501),v.MaxValueValidator(99950)])
    # need to validate it's an actual state lol...
    state = models.CharField(max_length=2)

class Store(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    # two stores can't have the same name...
    name = models.CharField(null=False, unique=True)
    # some kind of headcout?
    number_of_employees = models.PositiveIntegerField(validators=[v.MinValueValidator(1), v.MaxValueValidator(50)])
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    owner = models.PositiveIntegerField(validators=[v.MinValueValidator(1),v.MaxValueValidator(5)])
    

