from django import forms
from fit.models import progressChart

class bfCalcForm(forms.Form):
    #men - %BF = 495 / ( 1.0324 - 0.19077 * log10( waist - neck ) + 0.15456 * log10( height ) ) - 450
    height = forms.FloatField()
    waist = forms.FloatField()
    neck = forms.FloatField()
    hips = forms.FloatField()
    
class progress(forms.ModelForm):
    class Meta:
        model = progressChart
        exclude = ['date']