# Generated by Django 3.2.9 on 2021-11-20 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20211120_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=12, unique=True, verbose_name='телефон'),
        ),
    ]
