# Generated by Django 3.2.9 on 2021-12-03 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rental', '0003_auto_20211203_1222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='car_transmiossion',
            new_name='car_transmission',
        ),
    ]
