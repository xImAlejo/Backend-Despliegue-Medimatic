from django.db import models
from apps.user.models import User
from django.core.validators import MinValueValidator

# Create your models here.
class Activity(models.Model):
    id = models.AutoField(primary_key = True)
    task = models.CharField(max_length=100)
    asignation_date = models.DateTimeField('Asignation Date', auto_now=False, auto_now_add=False)
    limit_date = models.DateTimeField('Limit Date', auto_now=False,auto_now_add=False)
    detail = models.TextField()
    finalization_date = models.DateTimeField('Finalization Date', auto_now=False,auto_now_add=False,blank=True, null=True)
    area = models.CharField(max_length=100)
    priority = models.CharField(max_length=100) #agregarle un combobox
    state = models.CharField(max_length=100) #agregarle un combobox
    progress = models.CharField(max_length=100) #agregarle un combobox
    done = models.BooleanField('Done',default = False)
    observation = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)