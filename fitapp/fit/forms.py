from django import forms
from fit.models import progressChart

class bfCalcForm(forms.Form):
    height = forms.FloatField()
    waist = forms.FloatField()
    neck = forms.FloatField()
    hips = forms.FloatField()
    
class progress(forms.ModelForm):
    class Meta:
        model = progressChart
        exclude = ['date']