from django.db import models

# Create your models here.

class Product(models.Model):
    name    = models.TextField(max_length=30)
    price   = models.DecimalField(decimal_places=2,max_digits=5)
