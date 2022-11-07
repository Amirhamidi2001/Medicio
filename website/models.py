from django.db import models


class Appointment(models.Model):
    """This class is for an appointment with the doctor"""
    name = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.IntegerField()
    date = models.DateTimeField()
    department = models.CharField(max_length=60)
    doctor = models.CharField(max_length=60)
    message = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name


class Contact(models.Model):
    """This class is for users to contact the admin"""
    name = models.CharField(max_length=60)
    email = models.EmailField()
    subject = models.CharField(max_length=60)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    """This class is for website newsletter"""
    email = models.EmailField()

    def __str__(self):
        return self.email
