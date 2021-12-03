from io import BytesIO

from PIL import Image
from django.core.files import File
from django.db import models

# Отдел реализации
from django.utils.text import slugify

from apps.branch.models import Staff, Branch
from apps.thesaurus.models import Street, City, Payment, Category, Room

class Images(models.Model):
    realty = models.ForeignKey('Realty', on_delete=models.CASCADE, related_name='images')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    img = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title

class Realty(models.Model):
    '''Realty - сущность недвижимость'''
    class Meta:
        db_table = 'realties'
        verbose_name_plural = 'Объекты недвижимости'
        verbose_name = 'объект недвижимости'
        ordering = ("due_back",)

    RENT_STATUS =(
        ('free', 'Свободна'),
        ('rented', 'Сдана'),
        ('reserved', 'Зарезервирована'),
    )
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    description = models.TextField(help_text='описание краткое но емкое',max_length=500, blank=True, null=True)
    due_back = models.DateField('освободится', null=True, blank=True)
    rent_status = models.CharField('Статус', max_length=8, choices=RENT_STATUS, blank=True, default='free', help_text='Статус аренды')
    realty_number = models.CharField('Код объекта недвижимости', max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    street = models.ForeignKey(Street, on_delete=models.PROTECT,
                               related_name='realties', verbose_name='Улица')
    city = models.ForeignKey(City, on_delete=models.PROTECT,
                             related_name='realties', verbose_name='Город')
    postcode = models.CharField('Почтовый индекс', max_length=6)
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 related_name='realties', verbose_name='Категория недвижимости')
    rooms = models.ForeignKey(Room, on_delete=models.PROTECT,
                              related_name='realties', verbose_name='Количество комнат')
    rent = models.FloatField('Стоимость ренты')
    owner_number = models.ForeignKey('Owner', on_delete=models.PROTECT,
                                     related_name='realties', verbose_name='Код владельца недвижимости')
    staff_number = models.ForeignKey(Staff, on_delete=models.PROTECT,
                                     related_name='realties', verbose_name='Табельный номер сотрудника АН')
    branch_number = models.ForeignKey(Branch, on_delete=models.PROTECT,
                                      related_name='realties', verbose_name='Код филиала')

    def __str__(self):
        return self.realty_number

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail



class Owner(models.Model):
    '''Owner - сущность хозяин(арендодатель) недвижимости'''
    class Meta:
        db_table = 'owners'

    owner_number = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.ForeignKey(Street, on_delete=models.CASCADE, related_name='owners')
    tel_number = models.CharField(max_length=12)

    def __str__(self):
        return self.last_name

class Client(models.Model):
    '''Client - сущность клиент(арендатор) недвижимости'''
    class Meta:
        db_table = 'clients'

    client_number = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    tel_number = models.CharField(max_length=12)
    pref_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='clients')
    pref_rooms = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='clients')
    max_rent = models.FloatField()

    def __str__(self):
        return self.last_name

# Отдел контрактов

class Lease(models.Model):
    '''Lease - сущность контракт на аренду недвижимости'''
    class Meta:
        db_table = 'leases'

    PAID = 'yes'
    NOPAID = 'no'
    CHOICES_STATUS = (
        (PAID, 'yes'),
        (NOPAID, 'no')
    )
    lease_number = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    realty_number = models.ForeignKey(Realty, on_delete=models.CASCADE, related_name='leases')
    owner_number = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='leases')
    client_number = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='leases')
    rent = models.FloatField()
    payment_method = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='leases')
    deposit = models.FloatField()
    paid = models.CharField(max_length=10, choices=CHOICES_STATUS, default=NOPAID)
    rent_start = models.DateTimeField()
    rent_finish = models.DateTimeField()
    duration = models.PositiveSmallIntegerField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.lease_number)
        Realty.rent_status = 'rented'

        super(Lease, self).save(*args, **kwargs)

    def __str__(self):
        return self.lease_number

class Viewing(models.Model):
    '''Viewing - сущность просмотр недвижимости'''
    class Meta:
        db_table = 'viewings'
        ordering = ('-view_date',)

    client_number = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='viewings')
    realty_number = models.ForeignKey(Realty, on_delete=models.CASCADE, related_name='viewings')
    view_date = models.DateField()
    comment = models.CharField('комментарий', max_length=255)


    def __str__(self):
        return self.client_number.last_name

class Registration(models.Model):
    '''Registration - сущность регистрация '''
    class Meta:
        db_table = 'registrations'
        ordering = ('-date_joined',)

    client_number = models.ForeignKey(Client, on_delete=models.CASCADE,
                                      related_name='registrations')
    branch_number = models.ForeignKey(Branch, on_delete=models.CASCADE,
                                      related_name='registrations')
    staff_number = models.ForeignKey(Staff, on_delete=models.CASCADE,
                                     related_name='registrations')
    date_joined = models.DateField()


    def __str__(self):
        return self.client_number.last_name

















