# Generated by Django 3.2.9 on 2021-11-26 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='postcode',
            field=models.CharField(max_length=6, verbose_name='Почтовый индекс'),
        ),
    ]
