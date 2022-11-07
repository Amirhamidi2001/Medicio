from dataclasses import field
from django import forms
from .models import Appointment, Contact, Newsletter


class AppointmentForm(forms.ModelForm):
    """This class is for processing the appointment form"""

    class Meta:
        model = Appointment
        fields = '__all__'


class ContactForm(forms.ModelForm):
    """This class is for processing the contact form"""

    class Meta:
        model = Contact
        fields = '__all__'


class NewsletterForm(forms.ModelForm):
    """This class is for processing the newsletter form"""

    class Meta:
        model = Newsletter
        fields = '__all__'
