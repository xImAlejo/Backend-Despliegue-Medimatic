from django.db import models
from apps.product.models import Product
from django.core.validators import MinValueValidator

# Create your models here.
class Serie(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)