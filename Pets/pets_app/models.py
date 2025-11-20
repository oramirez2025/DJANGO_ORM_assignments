from django.db import models
from django.core import validators as v

class Owner(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(null=False)
    age = models.PositiveIntegerField(null=False)
    number_of_pets = models.PositiveIntegerField()

class Cat(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    breed = models.CharField(null=False)
    age = models.PositiveIntegerField(null=False)
    vaccinated = models.Boolean(null=False, default=False)

class Bird(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(null=False)
    age = models.PositiveIntegerField(null=False)
    vaccinated = models.Boolean(null=False, default=False)
    description = models.TextField()
    species = models.CharField(null=False)

class Dog(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    age = models.PositiveIntegerField(null=False)
    name = models.CharField(null=False)
    vaccinated = models.Boolean(null=False, default=False)
    breed = models.CharField(null=False)
    description = models.TextField()

class Exotic_Animal(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    region_of_origin = models.CharField(null=False)
    name = models.CharField(null=False)
    age = models.PositiveIntegerField(null=False)
    type_of_animal = models.CharField(null=False)
    vaccinated = models.Boolean(null=False, default=False)
