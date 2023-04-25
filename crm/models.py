from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Client(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)


class Contract(models.Model):
    sales_contact = models.ForeignKey(User, on_delete=models.SET_NULL)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()
    amount = models.FloatField()
    payment_due = models.DateTimeField()


class EventStatus(models.Model):
    name = models.CharField(max_length=255)


class Event(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    support_contact = models.ForeignKey(User, on_delete=models.SET_NULL)
    event_status = models.ForeignKey(EventStatus, on_delete=models.SET_NULL)
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField()
