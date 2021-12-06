from django.contrib.auth.models import User
from django.db import models


class Clients(models.Model):
    '''Client - сущность филиал агенства недвижимости'''
    class Meta:
        db_table = 'clients'
        ordering = ('name',)

    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='branch', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name