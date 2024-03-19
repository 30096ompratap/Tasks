from django.db import models

class Transaction(models.Model):
    date = models.DateField()
    desc = models.TextField(max_length = 100)
    credit = models.DecimalField(max_digits = 100 , decimal_places = 2 , null=True ,blank = True)
    debit = models.DecimalField(max_digits = 100 , decimal_places = 2 , null=True ,blank = True)
    running_balance = models.DecimalField(max_digits = 100 , decimal_places = 2 , null=True ,blank = True)

    def __str__(self) -> str:
        return str(self.date)+str(self.running_balance)
