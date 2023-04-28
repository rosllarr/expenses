from django.shortcuts import render
from datetime import date
from django.db.models import Sum

from .models import Monthly


def index(request):
    # Show table according to the current month.
    today = date.today()
    current_month = today.month

    start_date = date(today.year, current_month, 25)
    end_date = date(today.year, current_month+1, 25)

    entry_of_month = end_date

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

    return render(request, 'monthly/index.html',
                  {'entry_of_month': entry_of_month,
                   'entry_list': entry_list,
                   'income_of_month': income_of_month,
                   'expenses_of_month': expenses_of_month,
                   'remain_of_month': remain_of_month})
