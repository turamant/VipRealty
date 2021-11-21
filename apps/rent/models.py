from django.db import models

# Отдел реализации
from apps.branch.models import Staff, Branch
from apps.thesaurus.models import Street, City, Room, Payment, Category


class Property(models.Model):
    property_number = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    street = models.ForeignKey(Street, on_delete=models.CASCADE,
                               related_name='properties')
    city = models.ForeignKey(City, on_delete=models.CASCADE,
                             related_name='properties')
    postcode = models.CharField(max_length=6, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='realties')
    rooms = models.ForeignKey(Room, on_delete=models.CASCADE,
                              related_name='realties')
    rent = models.FloatField()
    owner_number = models.ForeignKey('PrivateOwner', on_delete=models.CASCADE,
                                     related_name='realties')
    staff_number = models.ForeignKey(Staff, on_delete=models.CASCADE,
                                     related_name='realties')
    branch_number = models.ForeignKey(Branch, on_delete=models.CASCADE,
                                      related_name='realties')


    class Meta:
        ordering = ('rooms',)

    def __str__(self):
        return self.property_number



class PrivateOwner(models.Model):
    owner_number = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.ForeignKey(Street, on_delete=models.CASCADE, related_name='privateowners')
    tel_number = models.CharField(max_length=12)

    def __str__(self):
        return self.last_name

class Client(models.Model):
    client_number = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    tel_number = models.CharField(max_length=12)
    pref_type = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='clients')
    pref_rooms = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='clients')
    max_rent = models.FloatField()

    def __str__(self):
        return self.last_name



# Отдел контрактов

class Lease(models.Model):
    PAID = 'yes'
    NOPAID = 'no'
    CHOICES_STATUS = (
        (PAID, 'yes'),
        (NOPAID, 'no')
    )
    lease_number = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    property_number = models.ForeignKey(PrivateOwner, on_delete=models.CASCADE, related_name='leases')
    client_number = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='leases')
    rent = models.FloatField()
    payment_method = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='leases')
    deposit = models.FloatField()
    paid = models.CharField(max_length=10, choices=CHOICES_STATUS, default=NOPAID)
    rent_start = models.DateTimeField()
    rent_finish = models.DateTimeField()
    duration = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.lease_number

class Viewing(models.Model):
    client_number = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='viewings')
    property_number = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='viewings')
    view_date = models.DateField()
    comment = models.CharField('комментарий', max_length=255)

    class Meta:
        ordering = ('-view_date',)

    def __str__(self):
        return self.client_number.last_name

class Registration(models.Model):
    client_number = models.ForeignKey(Client, on_delete=models.CASCADE,
                                      related_name='registrations')
    branch_number = models.ForeignKey(Branch, on_delete=models.CASCADE,
                                      related_name='registrations')
    staff_number = models.ForeignKey(Staff, on_delete=models.CASCADE,
                                     related_name='registrations')
    date_joined = models.DateField()

    class Meta:
        ordering = ('-date_joined',)

    def __str__(self):
        return self.client_number.last_name

















