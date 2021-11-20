# Generated by Django 3.2.9 on 2021-11-20 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='order',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='слаг'),
        ),
    ]
