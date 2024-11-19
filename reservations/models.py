from django.db import models

class Reservation(models.Model):
    FULL_NAME_MAX_LENGTH = 100
    CONTACT_METHOD_CHOICES = [
        ('email', 'Email'),
        ('phone', 'Phone'),
        ('either', 'Either'),
    ]

    SERVICE_CHOICES = [
        ('haircut', 'Haircut'),
        ('shave', 'Shave'),
        ('styling', 'Styling'),
    ]

    GENDER_CHOICES = [
        ('men', 'Men'),
        ('women', 'Women'),
        ('other', 'Other'),
    ]

    full_name = models.CharField(max_length=FULL_NAME_MAX_LENGTH)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    contact_method = models.CharField(max_length=10, choices=CONTACT_METHOD_CHOICES, default='email')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='other')  # New field
    service_required = models.CharField(max_length=10, choices=SERVICE_CHOICES, default='haircut')
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.full_name} - {self.service_required} on {self.date} at {self.time}"
