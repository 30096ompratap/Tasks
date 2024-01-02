from django.db import models

# Create your models here.

class Invoice(models.Model):
    CustomerName = models.CharField(max_length=30)
    Date = models.DateField()

    def __str__(self) -> str:
        return f"{self.CustomerName}"
    
class InvoiceDetail(models.Model):
    Invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE)
    Description = models.CharField(max_length=200)
    Quantity = models.PositiveIntegerField()
    Unit_Price = models.DecimalField(max_digits = 10 ,decimal_places = 2)
    Price = models.DecimalField(max_digits = 10 ,decimal_places = 2)

    def __str__(self) -> str:
        return super().__str__()

