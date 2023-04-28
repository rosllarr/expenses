from django.shortcuts import render
from datetime import date

from .models import Expenses


def index(request):
    # Show table according to the current month.
    today = date.today()
    current_month = today.month

    entry_list = Expenses.objects.filter(
        reserved_transection_date__month=current_month
        ).order_by('reserved_transection_date')

    return render(request, 'inex/index.html', {'entry_list': entry_list})
