# Generated by Django 3.2.9 on 2021-11-23 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('thesaurus', '__first__'),
        ('branch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_number', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('tel_number', models.CharField(max_length=12)),
                ('max_rent', models.FloatField()),
                ('pref_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='thesaurus.category')),
                ('pref_rooms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='thesaurus.room')),
            ],
            options={
                'db_table': 'clients',
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_number', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('tel_number', models.CharField(max_length=12)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owners', to='thesaurus.street')),
            ],
            options={
                'db_table': 'owners',
            },
        ),
        migrations.CreateModel(
            name='Realty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realty_number', models.CharField(max_length=100, unique=True, verbose_name='Код объекта недвижимости')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('postcode', models.CharField(max_length=6, unique=True, verbose_name='Почтовый индекс')),
                ('rent', models.FloatField(verbose_name='Стоимость ренты')),
                ('branch_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='realties', to='branch.branch', verbose_name='Код филиала')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='realties', to='thesaurus.category', verbose_name='Категория недвижимости')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='realties', to='thesaurus.city', verbose_name='Город')),
                ('owner_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='realties', to='rent.owner', verbose_name='Код владельца недвижимости')),
                ('rooms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='realties', to='thesaurus.room', verbose_name='Количество комнат')),
                ('staff_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='realties', to='branch.staff', verbose_name='Табельный номер сотрудника АН')),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='realties', to='thesaurus.street', verbose_name='Улица')),
            ],
            options={
                'db_table': 'realties',
                'ordering': ('rooms',),
            },
        ),
        migrations.CreateModel(
            name='Viewing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_date', models.DateField()),
                ('comment', models.CharField(max_length=255, verbose_name='комментарий')),
                ('client_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viewings', to='rent.client')),
                ('realty_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viewings', to='rent.realty')),
            ],
            options={
                'db_table': 'viewings',
                'ordering': ('-view_date',),
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
                ('branch_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='branch.branch')),
                ('client_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='rent.client')),
                ('staff_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='branch.staff')),
            ],
            options={
                'db_table': 'registrations',
                'ordering': ('-date_joined',),
            },
        ),
        migrations.CreateModel(
            name='Lease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lease_number', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('rent', models.FloatField()),
                ('deposit', models.FloatField()),
                ('paid', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=10)),
                ('rent_start', models.DateTimeField()),
                ('rent_finish', models.DateTimeField()),
                ('duration', models.PositiveSmallIntegerField()),
                ('client_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leases', to='rent.client')),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leases', to='thesaurus.payment')),
                ('realty_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leases', to='rent.owner')),
            ],
            options={
                'db_table': 'leases',
            },
        ),
    ]
