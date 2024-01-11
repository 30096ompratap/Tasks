from django.db import models

class YourModel(models.Model):
    timestamp = models.DateField()
    value = models.IntegerField()

    def __str__(self):
        return f"{self.timestamp} - {self.value}"

