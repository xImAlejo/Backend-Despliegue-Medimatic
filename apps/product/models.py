from django.db import models
from apps.user.models import User
from django.core.validators import MinValueValidator

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key = True)
    type = models.CharField(max_length=100)
    imported = models.CharField(max_length=100)
    description = models.TextField()
    brand = models.CharField(max_length=100)
    unit_price = models.FloatField()
    type_change = models.FloatField()
    bill_text = models.CharField(max_length=200, blank=True, null=True)
    date_bill = models.DateField('Bill Date', auto_now=False,auto_now_add=False, blank=True, null=True)
    model = models.CharField(max_length=100)
    origin = models.CharField(max_length=100, blank=True, null=True)
    date_manufacture = models.DateField('Manufacture Date', auto_now=False,auto_now_add=False, blank=True, null=True)
    minsa_code = models.CharField(max_length=100)
    minsa_description = models.TextField()
    supplier = models.CharField(max_length=200, blank=True, null=True)
    entry_point = models.CharField(max_length=100,blank=True, null=True)
    exit_point = models.CharField(max_length=100,blank=True, null=True)
    date = models.DateField('Date', auto_now=False,auto_now_add=False, blank=True, null=True)
    exit_date = models.DateField('Exit Date', auto_now=False,auto_now_add=False, blank=True, null=True)
    entry_guide = models.CharField(max_length=200, blank=True, null=True)
    exit_guide = models.CharField(max_length=200,blank=True, null=True)
    proyect = models.CharField(max_length=200,blank=True, null=True)
    responsible = models.CharField(max_length=100)
    coin_bill = models.CharField(max_length=100)
    quantity_total = models.IntegerField(null=True,blank=True)
    quantity_total_exit = models.IntegerField(null=True,blank=True)