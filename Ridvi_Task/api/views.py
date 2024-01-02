# from django.shortcuts import render


# from rest_framework import generics
# from .models import Invoice, InvoiceDetail
# from .serializers import InvoiceSerializer, InvoiceDetailSerializer

# class InvoiceListCreateView(generics.ListCreateAPIView):
#     queryset = Invoice.objects.all()
#     serializer_class = InvoiceSerializer

# class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Invoice.objects.all()
#     serializer_class = InvoiceSerializer

# class InvoiceDetailListCreateView(generics.ListCreateAPIView):
#     queryset = InvoiceDetail.objects.all()
#     serializer_class = InvoiceDetailSerializer

# invoices/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer

@api_view(['GET', 'POST'])
def invoice_list_create(request):
    if request.method == 'GET':
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def invoice_detail(request, pk):
    try:
        invoice = Invoice.objects.get(pk=pk)
    except Invoice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InvoiceSerializer(invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def invoice_detail_list_create(request):
    if request.method == 'GET':
        invoice_details = InvoiceDetail.objects.all()
        serializer = InvoiceDetailSerializer(invoice_details, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InvoiceDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
