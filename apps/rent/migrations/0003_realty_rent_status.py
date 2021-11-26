# Generated by Django 3.2.9 on 2021-11-23 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0002_auto_20211123_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='realty',
            name='rent_status',
            field=models.CharField(blank=True, choices=[('free', 'Свободна'), ('rented', 'Сдана'), ('reserved', 'Зарезервирована')], default='free', help_text='Статус аренды', max_length=8, verbose_name='Статус'),
        ),
    ]
