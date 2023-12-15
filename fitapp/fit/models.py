from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class weightModel(models.Model):
    date = models.DateField(auto_now=True)
    bodyFat = models.DecimalField("Enter Bodyfat Percentage", max_digits=4,decimal_places=2)
    weight = models.IntegerField("Enter weight")
    
    class Meta:
        db_table = "weight"

class liftModel(models.Model):
    date = models.DateField(auto_now=True)
    benchPR = models.IntegerField("Enter new bench press record", null=True, blank=True)
    ohpPR = models.IntegerField("Enter new overhead press record", null=True, blank=True)
    squatPR = models.IntegerField("Enter new squat record", null=True, blank=True)
    deadliftPR = models.IntegerField("Enter new deadlift record", null=True, blank=True)
    
    def clean(self):
        #add validation that at least 1 lift entry is set, prevents false entries
        
        entries = [self.benchPR, self.ohpPR, self.squatPR, self.deadliftPR]
        if not all(entries):
            raise ValidationError('One must be filled')

    class Meta:
        db_table = "lifts"


class recipeModel(models.Model):
    name = models.CharField(max_length=50)
    calories = models.IntegerField()
    protein = models.DecimalField(max_digits=4, decimal_places=1)
    fat = models.DecimalField(max_digits=4, decimal_places=1)
    carbs = models.DecimalField(max_digits=4, decimal_places=1)
    link = models.URLField(max_length=200)

    class Meta:
        db_table = "recipes"