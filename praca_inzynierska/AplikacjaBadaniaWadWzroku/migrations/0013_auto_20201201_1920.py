# Generated by Django 3.1.3 on 2020-12-01 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AplikacjaBadaniaWadWzroku', '0012_auto_20201201_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information1',
            name='disease_pl',
        ),
        migrations.RemoveField(
            model_name='information1',
            name='disease_ru',
        ),
    ]
