from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Supplier
from .forms import CustomerForm, SupplierForm


def index(request):
    return render(request, 'core/index.html')

def list_customers(request):
    customers = Customer.objects.all()
    return render(request, 'core/list_customers.html', {'customers': customers})

def list_suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, 'core/list_suppliers.html', {'suppliers': suppliers})

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_customers')
    else:
        form = CustomerForm()
    return render(request, 'core/add_customer.html', {'form': form})

def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_suppliers')
    else:
        form = SupplierForm()
    return render(request, 'core/add_supplier.html', {'form': form})