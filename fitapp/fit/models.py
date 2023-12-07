from django.db import models

# Create your models here.
class progressChart(models.Model):
    date = models.DateField(auto_now=True)
    bodyFat = models.DecimalField("Enter Bodyfat Percentage", max_digits=4,decimal_places=2)
    weight = models.IntegerField("Enter weight")
    
    class Meta:
        db_table = "progress"