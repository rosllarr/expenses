from django.db import models
from datetime import date


class Expenses(models.Model):
    title = models.CharField(max_length=200)
    reserved_transection_date = models.DateField('date reserved', default=None)
    transection_date = models.DateField('action date', default=None)
    income = models.DecimalField(
        'income', max_digits=7, decimal_places=0, default=0)
    expenses = models.DecimalField(
        'expenses', max_digits=7, decimal_places=0, default=0)
    reserved_expenses = models.DecimalField(
        'reserved expenses', max_digits=7, decimal_places=0, default=0)

    def __str__(self):
        return self.title

    def is_already_occurred(self):
        return self.transection_date != date(1970, 1, 1)
