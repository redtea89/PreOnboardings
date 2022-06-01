from django.db import models


class Group(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)


class Restaurant(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)


class Pos(models.Model):
    PAYMENTS = [
        ('CARD', 'CARD'),
        ('CASH', 'CASH'),
        ('PHONE', 'PHONE'),
        ('BITCOIN', 'BITCOIN')
        ]
    timestamp = models.DateTimeField()
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    price = models.IntegerField()
    number_of_party = models.IntegerField()
    payment = models.CharField(max_length=20, choices=PAYMENTS)