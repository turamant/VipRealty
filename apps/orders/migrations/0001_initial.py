# Generated by Django 3.2.9 on 2021-11-23 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rent', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('slug', models.SlugField(max_length=100)),
                ('phone_number', models.CharField(max_length=12, verbose_name='Телефон')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания:')),
                ('comment', models.CharField(max_length=255, verbose_name='Комментарий')),
                ('realty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='rent.realty', verbose_name='Заявка')),
            ],
            options={
                'db_table': 'orders',
                'ordering': ('create_date',),
            },
        ),
    ]
