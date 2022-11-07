from .forms import AppointmentForm, ContactForm, NewsletterForm
from django.shortcuts import render


def index_view(request):
    if request.method == 'POST':
        appointment_form = AppointmentForm(request.POST)
        contact_form = ContactForm(request.POST)
        newsletter_form = NewsletterForm(request.POST)
        
        if appointment_form.is_valid():
            appointment_form.save()
        elif contact_form.is_valid():
            contact_form.save()
        elif newsletter_form.is_valid():
            newsletter_form.save()

    appointment_form = AppointmentForm()
    contact_form = ContactForm()
    newsletter_form = NewsletterForm()

    context = {
        'aform':appointment_form,
        'cform':contact_form,
        'nform':newsletter_form,
    }
    return render(request, 'index.html', context)
