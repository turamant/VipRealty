# Generated by Django 3.2.9 on 2021-12-03 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0010_rename_post_images_realty'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='realty',
            options={'ordering': ('due_back',), 'verbose_name': 'объект недвижимости', 'verbose_name_plural': 'Объекты недвижимости'},
        ),
    ]