from django.db import models


class Expenses(models.Model):
    reserved_transection_date = models.DateField('date reserved')
    transection_date = models.DateField('action date')
    income = models.DecimalField('income', max_digits=7, decimal_places=7)
    expenses = models.DecimalField('expenses', max_digits=7, decimal_places=7)
