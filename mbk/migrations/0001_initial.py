# Generated by Django 2.0.9 on 2018-11-12 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12)),
                ('nombre', models.CharField(max_length=200)),
                ('comuna', models.CharField(max_length=200)),
                ('nrotarjeta', models.CharField(max_length=200)),
                ('contraseña', models.CharField(max_length=200)),
            ],
        ),
    ]
