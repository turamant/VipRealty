# Generated by Django 3.2.9 on 2021-12-06 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('thesaurus', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_number', models.CharField(max_length=100, unique=True, verbose_name='Филиал')),
                ('postcode', models.CharField(max_length=6, verbose_name='Почтовый индекс')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branchs', to='thesaurus.city')),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='branch', to=settings.AUTH_USER_MODEL)),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branchs', to='thesaurus.street')),
            ],
            options={
                'db_table': 'branchs',
                'ordering': ('street',),
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_number', models.CharField(max_length=100, unique=True, verbose_name='Табельный номер')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('sex', models.CharField(choices=[('man', 'М'), ('woman', 'Ж')], default='man', max_length=10, verbose_name='Пол')),
                ('date_of_birthday', models.DateField(verbose_name='Дата рожения')),
                ('salary', models.FloatField(verbose_name='Зарплата')),
                ('branch_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staffs', to='branch.branch')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staffs', to='thesaurus.position')),
            ],
            options={
                'db_table': 'staffs',
                'ordering': ('last_name',),
            },
        ),
    ]
