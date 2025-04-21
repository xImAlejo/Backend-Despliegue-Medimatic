from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Coordination(models.Model):
    id = models.AutoField(primary_key = True)
    clientname = models.CharField(max_length=100) 
    activity_detail = models.TextField()
    arrival_date = models.DateTimeField('Arrival Date', auto_now=False, auto_now_add=False)
    final_date = models.DateTimeField('Final Date', auto_now=False, auto_now_add=False,blank=True, null=True)
    initial_date = models.DateTimeField('Initial Date', auto_now=False, auto_now_add=False)
    priority = models.CharField(max_length=100)
    job_order = models.CharField(max_length=100)
    state = models.CharField(max_length=100) 
    done = models.BooleanField('Done',default = False)
    observation = models.TextField(blank=True, null=True)
    register_date = models.DateTimeField('Register Date', auto_now=False, auto_now_add=True)