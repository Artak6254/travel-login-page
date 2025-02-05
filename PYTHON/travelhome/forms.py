from django import forms
from .models import Booking, Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['place_name', 'number_of_guests', 'arrival_date', 'leaving_date']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email_name', 'email', 'people_number', 'subject', 'message']


class CreateUserForm(UserCreationForm):
    model = User
    fields = ['username','email','password1','password2']
