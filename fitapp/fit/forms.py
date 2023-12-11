from django import forms
from fit.models import progressModel, liftModel

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
        