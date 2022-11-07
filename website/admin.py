from django.contrib import admin
from .models import Contact, Appointment, Newsletter


class AppointmentAdmin(admin.ModelAdmin):
    """
    This class is for displaying appointment in administration
    """
    date_hierarchy = 'created_date'
    list_display = ('name', 'department', 'email')
    list_filter = ('department', 'doctor')
    search_fields = ('name', 'message', 'department')


class ContactAdmin(admin.ModelAdmin):
    """
    This class is for displaying contact in administration
    """
    date_hierarchy = 'created_date'
    list_display = ('name', 'email')
    list_filter = ('email',)
    search_fields = ('name', 'message')

admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter)
