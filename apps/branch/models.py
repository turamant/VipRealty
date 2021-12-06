from django.contrib.auth.models import User
from django.db import models

from apps.thesaurus.models import Street, City, Position


class Branch(models.Model):
    '''Branch - сущность филиал агенства недвижимости'''
    class Meta:
        db_table = 'branchs'
        ordering = ('name',)

    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='branch', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Staff(models.Model):
    '''Staff - сущность персонал агентства недвижимости '''
    class Meta:
        db_table = 'staffs'
        ordering = ('last_name',)

    MAN = 'man'
    WOMAN = 'woman'
    CHOICES_STATUS = (
        (MAN, 'М'),
        (WOMAN, 'Ж')
    )
    staff_number = models.CharField('Табельный номер', max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    position = models.ForeignKey(Position, on_delete=models.CASCADE,
                                 related_name='staffs')
    sex = models.CharField('Пол', max_length=10, choices=CHOICES_STATUS, default=MAN)
    date_of_birthday = models.DateField('Дата рожения')
    salary = models.FloatField('Зарплата')
    branch_name = models.ForeignKey(Branch, on_delete=models.CASCADE,
                                      related_name='staffs')

    def __str__(self):
        return self.last_name


