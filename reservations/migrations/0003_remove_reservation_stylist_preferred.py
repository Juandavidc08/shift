# Generated by Django 5.1.3 on 2024-11-11 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_rename_name_reservation_full_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='stylist_preferred',
        ),
    ]