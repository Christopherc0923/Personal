from django.db import models
from datetime import datetime
# Create your models here.

class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100, default='U')
    price = models.FloatField()
    change = models.FloatField(default=0)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.symbol