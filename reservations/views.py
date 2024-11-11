from django.shortcuts import render, redirect
from .forms import ReservationForm
from django.utils import timezone
from django.contrib import messages

def make_reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Ensure date and time are not in the past
            reservation_date = form.cleaned_data['date']
            reservation_time = form.cleaned_data['time']
            if reservation_date < timezone.now().date() or \
               (reservation_date == timezone.now().date() and reservation_time <= timezone.now().time()):
                messages.error(request, "Please select a future date and time.")
            else:
                form.save()
                messages.success(request, "Reservation successfully created.")
                return redirect('reservation_success')
    else:
        form = ReservationForm()
    return render(request, 'reservations/make_reservation.html', {'form': form})
