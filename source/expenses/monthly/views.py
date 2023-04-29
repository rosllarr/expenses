from django.shortcuts import redirect, render
from datetime import date
from django.db.models import Sum
from django.urls import reverse
from django.db.models import Q

from .models import Monthly


def yearly(request, year_id):
    # Show table according to the year
    year = year_id

    start_date = date(year-1, 12, 25)
    end_date = date(year, 11, 25)

    entry_of_expenses = Monthly.objects.filter(
        transection_date__gte=start_date,
        transection_date__lte=end_date,
        tags__name='year').filter(tags__name='expenses')

    expenses_of_year = Monthly.objects.filter(
        transection_date__gte=start_date,
        transection_date__lte=end_date,
        tags__name='year').filter(tags__name='expenses'
                                  ).aggregate(Sum('cost'))['cost__sum']

    contexts = {
        'entry_of_expenses': entry_of_expenses,
        'expenses_of_year': expenses_of_year
    }

    return render(request, 'monthly/yearly.html', contexts)


def monthly(request, month_id):
    # Show table according to the month_id.
    month = month_id
    year = date.today().year

    start_date = date(year, month-1, 25)
    end_date = date(year, month, 24)

    entry_of_month = end_date
    previous_month = month - 1

    entry_list = Monthly.objects.filter(
        transection_date__gte=start_date,
        transection_date__lte=end_date
        ).order_by('transection_date')

    income_of_month = Monthly.objects.filter(
        transection_date__gte=start_date,
        transection_date__lte=end_date,
        tags__name='income'
        ).aggregate(Sum('cost'))['cost__sum']

    expenses_of_month = Monthly.objects.filter(
        transection_date__gte=start_date,
        transection_date__lte=end_date,
        tags__name='expenses'
    ).aggregate(Sum('cost'))['cost__sum']

    remain_of_month = income_of_month - expenses_of_month

    return render(request, 'monthly/monthly.html',
                  {'entry_of_month': entry_of_month,
                   'entry_list': entry_list,
                   'income_of_month': income_of_month,
                   'expenses_of_month': expenses_of_month,
                   'remain_of_month': remain_of_month,
                   'previous_month': previous_month})


def index(request):
    # Show table according to the current month.
    today = date.today()
    current_month = today.month + 1

    return redirect(reverse('monthly:monthly', args=[current_month]))
