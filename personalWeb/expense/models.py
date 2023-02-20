from django.db import models

# Create your models here.

class Expense(models.Model):
    date = models.DateField()
    category = models.CharField(max_length=50)
    description = models.TextField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)