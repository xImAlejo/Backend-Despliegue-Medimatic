from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Proyect(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100) 
    stage = models.CharField(max_length=100)