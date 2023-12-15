from django import forms
from fit.models import weightModel, liftModel, recipeModel

#create forms for view/inputs in html

#form for bodyfat calculator

class bfCalcForm(forms.Form):
    height = forms.FloatField()
    waist = forms.FloatField()
    neck = forms.FloatField()
    hips = forms.FloatField(initial=0.0)
    
#form for inputing bodyweight/fat percentage, pull from model

class weightForm(forms.ModelForm):
    class Meta:
        model = weightModel
        
        #skip date due to auto input
        exclude = ['date']
        
#form for inputing lift PR, pull from model

class liftForm(forms.ModelForm):
    class Meta:
        model = liftModel
        
        #skip date due to auto input
        exclude = ['date']

#form to select routine suggestion

class routineForm(forms.Form):
    CHOICES = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    )

    routine_choice = forms.ChoiceField(choices=CHOICES)

#form to select muscle group

class targetForm(forms.Form):
    CHOICES = (
        ('forearms', 'Forearms'),
        ('biceps', 'Biceps'),
        ('triceps', 'Triceps'),
        ('shoulders', 'Shoulders'),
        ('chest', 'Chest'),
        ('back', 'Back'),
        ('quads', 'Quads'),
        ('hamstrings', 'Hamstrings'),
        ('calves', 'Calves')
    )

    target_choice = forms.ChoiceField(choices=CHOICES)

#form to display recipes

class recipeForm(forms.ModelForm):
    class Meta:
        model = recipeModel
        fields = '__all__'