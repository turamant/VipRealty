# Generated by Django 3.2.9 on 2021-12-01 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0007_realty_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realty',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]