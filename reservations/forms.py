from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'full_name', 'email', 'phone_number', 'contact_method', 
            'service_required', 'date', 'time', 'additional_details'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'contact_method': forms.RadioSelect,  # Radio buttons for contact method
        }
        labels = {
            'full_name': 'Full Name',
            'email': 'E-mail',
            'phone_number': 'Phone Number',
            'contact_method': 'Preferred method of contact',
            'service_required': 'Service required',
            'date': 'Date',
            'time': 'Time',
            'additional_details': 'Other details you may wish to highlight',
        }
