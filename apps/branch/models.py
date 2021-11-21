from django.db import models

from apps.thesaurus.models import Street, City, Position, Sex


class Branch(models.Model):
    branch_number = models.CharField('отделение', max_length=100, unique=True)
    street = models.ForeignKey(Street, on_delete=models.CASCADE, related_name='realties')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='realties')
    postcode = models.CharField('индекс', max_length=6, unique=True)

    class Meta:
        ordering = ('street',)

    def __str__(self):
        return self.branch_number

class Staff(models.Model):
    staff_number = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    position = models.ForeignKey(Position, on_delete=models.CASCADE,
                                 related_name='staffs')
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE, related_name='staffs')
    date_of_birthday = models.DateField()
    salary = models.FloatField()
    branch_number = models.ForeignKey(Branch, on_delete=models.CASCADE,
                                      related_name='staffs')

    class Meta:
        ordering = ('last_name',)

    def __str__(self):
        return self.last_name


