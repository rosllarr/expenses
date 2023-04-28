from django.shortcuts import render
from datetime import date
from django.db.models import Sum

from .models import Expenses


def index(request):
    # Show table according to the current month.
    today = date.today()
    current_month = today.month

    start_date = date(today.year, current_month, 25)
    end_date = date(today.year, current_month+1, 25)

    entry_list = Expenses.objects.filter(
        reserved_transection_date__gte=start_date,
        reserved_transection_date__lte=end_date
        ).order_by('reserved_transection_date')

    income_of_month = Expenses.objects.filter(
        reserved_transection_date__gte=start_date,
        reserved_transection_date__lte=end_date
    ).aggregate(Sum('income'))['income__sum']

    reserved_expenses_of_month = Expenses.objects.filter(
        reserved_transection_date__gte=start_date,
        reserved_transection_date__lte=end_date
    ).aggregate(Sum('reserved_expenses'))['reserved_expenses__sum']

    expenses_of_month = Expenses.objects.filter(
        reserved_transection_date__gte=start_date,
        reserved_transection_date__lte=end_date
    ).aggregate(Sum('expenses'))['expenses__sum']

    remain_of_month = income_of_month - reserved_expenses_of_month

    return render(request, 'inex/index.html',
                  {'entry_list': entry_list,
                   'income_of_month': income_of_month,
                   'reserved_expenses_of_month': reserved_expenses_of_month,
                   'remain_of_month': remain_of_month})
