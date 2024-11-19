# Generated by Django 5.1.3 on 2024-11-19 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_remove_reservation_additional_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='gender',
            field=models.CharField(choices=[('men', 'Men'), ('women', 'Women'), ('other', 'Other')], default='other', max_length=10),
        ),
    ]
