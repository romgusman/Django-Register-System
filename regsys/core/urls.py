from django.urls import path
from .views import list_customers,list_suppliers,add_customer,add_supplier, index

urlpatterns = [
    path('', index, name='index'),
    path('customers/', list_customers, name='list_customers'),
    path('suppliers/', list_suppliers, name='list_suppliers'),
    path('customers/add/', add_customer, name='add_customer'),
    path('suppliers/add/', add_supplier, name='add_supplier'),
    ]