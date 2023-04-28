from django.db import models
from datetime import date


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Monthly(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=7, decimal_places=0, default=0)
    transection_date = models.DateField(default=date(1970, 1, 1))
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def is_already_occurred(self):
        return self.transection_date <= date.today()
