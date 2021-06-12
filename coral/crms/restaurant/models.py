from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Food(models.Model):
    CATEGORY = (
        ('Breakfast', 'Breakfast'),
        ('Launch', 'Launch'),
        ('Dinner', 'Dinner'),
        ('Dessert', 'Dessert'),
        ('Salad', 'Salad'),
        ('Drink', 'Drink'),
    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='images/', default='default.jpg')

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(User, null=True, on_delete = models.SET_NULL,)
    food = models.CharField(max_length=200, null=True)
    quantity = models.IntegerField(null=True, default=1)
    price = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    email = models.CharField(max_length=200, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=15, blank=True, null=True)
    zip_code = models.CharField(max_length=200, null=True)
    is_paid = models.BooleanField(default=False, null=True)
    is_delivered = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.food + " ordered by " + self.email

class Reservation(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.name


class TableReservation(models.Model):
    type = models.ForeignKey(Reservation, null=True, on_delete = models.SET_NULL)
    customer = models.ForeignKey(User, null=True, on_delete = models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    no_people = models.IntegerField(null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=200, null=True)
    comment = models.TextField(null=True)
    price = models.FloatField(null=True)
    is_paid = models.BooleanField(default=False, null=True)
    is_approved = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.type.name + " booked by " + self.email


    def get_absolute_url(self):
        return reverse('reservation-confirmation', args=[str(self.id)])
    

class Activity(models.Model):
    name = models.CharField(max_length=200, null=True)
    picture = models.ImageField(upload_to='images/recreations/', default='default.jpg')
    price = models.FloatField(null=True)

    class Meta:
        verbose_name_plural = 'Activities'

    def __str__(self):
        return self.name


class Recreation(models.Model):
    activity = models.ForeignKey(Activity, null=True, on_delete = models.SET_NULL)
    customer = models.ForeignKey(User, null=True, on_delete = models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True, null=True)
    no_days = models.IntegerField(null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=200, null=True)
    comment = models.TextField(null=True)
    price = models.FloatField(null=True)
    is_paid = models.BooleanField(default=False, null=True)
    is_approved = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.activity.name

    def get_absolute_url(self):
        return reverse('recreation-confirmation', args=[str(self.id)])

    

