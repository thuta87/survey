from django.db import models

# Create your models here.
class Para(models.Model):
    paraid = models.AutoField(primary_key=True)
    dept_name=models.CharField(max_length=500)

class Survey(models.Model):
    tranid = models.AutoField(primary_key=True)
    paraid = models.ForeignKey('para',on_delete=models.CASCADE,)
    points = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    desc = models.CharField(max_length=500)
    contact_txt=models.CharField(max_length=500)
    timestamp= models.TimeField(auto_now_add=True)
        