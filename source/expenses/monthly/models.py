from django.db import models
from datetime import date


class Tags(models.Model):
    reserved = models.BooleanField(default=True)
    income = models.BooleanField(default=False)
    expenses = models.BooleanField(default=True)


class Monthly(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=7, decimal_places=0, default=0)
    transection_date = models.DateField(default=date(1970-1-1))
