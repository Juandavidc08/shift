# urls.py
from django.urls import path
from . import views  # Import views correctly

urlpatterns = [
    path('reserve/', views.make_reservation, name='make_reservation'),  # Correct usage of views.make_reservation
    path('success/', views.reservation_success, name='reservation_success'),  # Success page
]
