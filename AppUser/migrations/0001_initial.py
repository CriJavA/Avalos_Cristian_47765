# Generated by Django 4.2.5 on 2023-10-04 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Marca', models.CharField(max_length=60)),
                ('Modelo', models.CharField(max_length=60)),
                ('Year', models.CharField(max_length=4)),
                ('Color', models.CharField(max_length=20)),
                ('Precio', models.FloatField(max_length=10)),
                ('Descrip', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='MainUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NickName', models.CharField(max_length=60)),
                ('UserName', models.CharField(max_length=60)),
                ('UserDate', models.DateField()),
                ('UserAddress', models.CharField(max_length=60)),
                ('UserPass', models.CharField(max_length=20)),
                ('UserEmail', models.EmailField(max_length=254)),
                ('UserTnum', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo', models.CharField(max_length=30)),
                ('Subtipo', models.CharField(max_length=30)),
                ('Precio', models.FloatField(max_length=10)),
                ('Descrip', models.CharField(max_length=500)),
            ],
        ),
    ]
