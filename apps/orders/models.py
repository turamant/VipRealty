from django.db import models

from apps.rent.models import Realty


class Order(models.Model):
    '''Order - сущность заявка на просмотр объекта недвижимости'''
    class Meta:
        db_table = 'orders'
        ordering = ('create_date',)

    realty = models.ForeignKey(Realty, on_delete=models.CASCADE, related_name='orders',
                               verbose_name='Заявка')
    name = models.CharField('Имя', max_length=100)
    slug = models.SlugField(max_length=100)
    phone_number = models.CharField('Телефон', max_length=12)
    create_date = models.DateTimeField('Дата создания:', auto_now_add=True)
    comment = models.CharField('Комментарий', max_length=255)

    def __str__(self):
        return self.name
