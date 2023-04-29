from django.shortcuts import redirect, render
from datetime import date
from django.db.models import Sum
from django.urls import reverse

from .models import Monthly


def yearly(request, year_id):
    # Show table according to the year
    year = year_id

    start_date = date(year-1, 12, 25)
    end_date = date(year, 11, 25)

    entry_of_monthly_savings = Monthly.objects.filter(
        transection_date__gte=start_date,
        transection_date__lte=end_date,
        tags__name='year').filter(tags__name='savings')

    monthly_savings_of_year = Monthly.objects.filter(
        transection_date__gte=start_date,
        transection_date__lte=end_date,
        tags__name='year').filter(tags__name='savings'
                                  ).aggregate(Sum('cost'))['cost__sum']

    savings_in_year = Monthly.objects.filter(
        transection_date__gte=start_date,
        transection_date__lte=end_date,
        tags__name='year'
        ).filter(tags__name='savings'
                 ).exclude(tags__name='car_insurance'
                           ).aggregate(Sum('cost'))['cost__sum']

    previous_savings = Monthly.objects.filter(tags__name='previous_savings'
                                              ).values().get()['cost']

    total_savings = savings_in_year + previous_savings

    car_insurance = Monthly.objects.filter(
        transection_date__gte=start_date,
        transection_date__lte=end_date,
        tags__name='car_insurance').aggregate(Sum('cost'))['cost__sum']

    total_savings_with_car_insurance = total_savings + car_insurance

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
        'entry_of_monthly_savings': entry_of_monthly_savings,
        'monthly_savings_of_year': monthly_savings_of_year,
        'savings_in_year': savings_in_year,
        'previous_savings': previous_savings,
        'total_savings': total_savings,
        'car_insurance': car_insurance,
        'total_savings_with_car_insurance': total_savings_with_car_insurance,
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
