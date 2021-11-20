from django.db import models

from apps.rent.models import Realty


class Order(models.Model):
    real = models.ForeignKey(Realty, on_delete=models.CASCADE,
                             related_name='orders',
                             verbose_name='недвижимость')
    name = models.CharField('имя', max_length=100)
    slug = models.SlugField('слаг', max_length=100)
    phone_number = models.CharField('телефон', max_length=12)
    create_date = models.DateTimeField('дата', auto_now_add=True)

    def __str__(self):
        return self.name
