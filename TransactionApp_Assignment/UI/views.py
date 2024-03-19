from django.shortcuts import render , redirect
from datetime import datetime
from .models import Transaction
from decimal import Decimal

# Create your views here.
def home(request):
    transactions = Transaction.objects.all().order_by('-date')
    return render(request,'home.html',{'transactions':transactions})

def transaction(request):
    if request.method == "POST":
        last_transaction = Transaction.objects.last()
        if last_transaction:
            current_balance = Decimal(last_transaction.running_balance)
        else:
            current_balance = Decimal(0.0)

        current_date = datetime.now()
        desc = request.POST.get('Description')
        transaction_type = request.POST.get('type')
        amount = Decimal(request.POST.get('amount'))

        if transaction_type == 'credit':
            current_balance += amount
            transaction = Transaction.objects.create(date=current_date,desc = desc,credit=amount,debit=0.00,running_balance=current_balance)
        else:
            current_balance -= amount
            transaction = Transaction.objects.create(date=current_date,desc = desc,credit=0.00,debit=amount,running_balance=current_balance)

        transaction.save()
        return redirect('/')
    return render(request,'transaction.html')