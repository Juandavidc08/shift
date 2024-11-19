from django import forms
from .models import Reservation
from datetime import datetime, date

class ReservationForm(forms.ModelForm):
    # Add email field with validation
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        error_messages={'invalid': 'Enter a valid email address'}
    )

    class Meta:
        model = Reservation
        fields = [
            'full_name', 'email', 'phone_number', 'contact_method',
            'gender', 'service_required', 'date', 'time'
        ]
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'min': date.today().strftime('%Y-%m-%d')  # Prevent past dates
            }),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'contact_method': forms.RadioSelect,
            'gender': forms.RadioSelect,
        }
        labels = {
            'full_name': 'Full Name',
            'email': 'E-mail',
            'phone_number': 'Phone Number',
            'contact_method': 'Preferred Method of Contact',
            'gender': 'Gender',
            'service_required': 'Service Required',
            'date': 'Date',
            'time': 'Time',
        }

    def clean(self):
        cleaned_data = super().clean()
        selected_date = cleaned_data.get('date')
        selected_time = cleaned_data.get('time')
        
        if selected_date and selected_time:
            # Combine date and time into a datetime object for comparison
            selected_datetime = datetime.combine(selected_date, selected_time)
            current_datetime = datetime.now()

            if selected_datetime < current_datetime:
                # Display custom error for past time selection
                raise forms.ValidationError(
                    "The selected time has already passed. Please choose a future time.",
                    code='invalid_time'
                )
        
        return cleaned_data
