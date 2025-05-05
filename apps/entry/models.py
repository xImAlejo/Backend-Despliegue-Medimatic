from django.db import models
from apps.serie.models import Serie

# Create your models here.
class Entry(models.Model):
    id = models.AutoField(primary_key = True)
    quantity = models.IntegerField(null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)