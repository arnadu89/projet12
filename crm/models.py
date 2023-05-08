from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Team(models.IntegerChoices):
        MANAGEMENT = 1, "MANAGEMENT"
        SALES = 2, "SALES"
        SUPPORT = 3, "SUPPORT"

    team = models.PositiveSmallIntegerField(
        choices=Team.choices
    )


class Client(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    sales_contact = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def complete_name(self):
        return f"{self.last_name} {self.first_name}"

    def __repr__(self):
        return f"Client {self.complete_name()}"

    def __str__(self):
        return self.__repr__()


class Contract(models.Model):
    sales_contact = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
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
    support_contact = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    event_status = models.ForeignKey(EventStatus, null=True, on_delete=models.SET_NULL)
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField()
