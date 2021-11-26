from django.db import models


class City(models.Model):
    '''City - сущность город'''
    class Meta:
        db_table = 'cities'

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Street(models.Model):
    '''Street - сущность улица'''
    class Meta:
        db_table = 'streets'
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    '''Category - сущность категория недвижимости'''
    class Meta:
        db_table = 'categories'
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    '''Room - сущность комната'''
    class Meta:
        db_table = 'rooms'
    number = models.PositiveSmallIntegerField(2)


    def __str__(self):
        return str(self.number)

class Payment(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name
