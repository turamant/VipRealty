# Generated by Django 3.2.9 on 2021-11-21 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('thesaurus', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_number', models.CharField(max_length=100, unique=True, verbose_name='отделение')),
                ('postcode', models.CharField(max_length=6, unique=True, verbose_name='индекс')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='realties', to='thesaurus.city')),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='realties', to='thesaurus.street')),
            ],
            options={
                'ordering': ('street',),
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_number', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('date_of_birthday', models.DateField()),
                ('salary', models.FloatField()),
                ('branch_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staffs', to='branch.branch')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staffs', to='thesaurus.position')),
                ('sex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staffs', to='thesaurus.sex')),
            ],
            options={
                'ordering': ('last_name',),
            },
        ),
    ]
