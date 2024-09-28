from django import forms
from .models import Customer, Supplier

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'adress', 'cpf']

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'email', 'phone', 'adress', 'cnpj']