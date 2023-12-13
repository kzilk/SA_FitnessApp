from django import forms
from fit.models import progressModel, liftModel, recipeModel

class bfCalcForm(forms.Form):
    height = forms.FloatField()
    waist = forms.FloatField()
    neck = forms.FloatField()
    hips = forms.FloatField(initial=0.0)
    
class progressForm(forms.ModelForm):
    class Meta:
        model = progressModel
        exclude = ['date']
        
class liftForm(forms.ModelForm):
    class Meta:
        model = liftModel
        exclude = ['date']


class routineForm(forms.Form):
    CHOICES = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    )

    routine_choice = forms.ChoiceField(choices=CHOICES)

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


class recipeForm(forms.ModelForm):
    class Meta:
        model = recipeModel
        fields = '__all__'