from django.urls import path
from .views import (
    invoice_list_create,
    invoice_detail,
    invoice_detail_list_create
)

urlpatterns = [
    path('invoices/', invoice_list_create, name='invoice-list-create'),
    path('invoices/<int:pk>/', invoice_detail, name='invoice-detail'),
    path('invoice-details/', invoice_detail_list_create, name='invoice-detail-list-create'),
]
