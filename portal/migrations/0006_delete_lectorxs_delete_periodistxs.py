# Generated by Django 4.0.4 on 2022-06-01 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_remove_periodistxs_leg_periodistxs_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Lectorxs',
        ),
        migrations.DeleteModel(
            name='Periodistxs',
        ),
    ]
