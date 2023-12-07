from django.shortcuts import render
from django.views import View
from .forms import bfCalcForm, progress
from .models import progressChart
import math
    
class Index(View):
    def get(self, request):
        form = bfCalcForm()
        prog = progress()
        data = progressChart.objects.all()
        print(data)
        context = {'form':form, 'progress':prog, 'data':data}       
        return render(request, 'fit/index.html', context) 
    
    def post(self, request):
        #handle bfCalculator
        form = bfCalcForm(request.POST)
        bfResult = None

        if form.is_valid():
            #process bfCalc data and perform calculations
            bfHeight = int(form.cleaned_data['height'])
            bfWaist = int(form.cleaned_data['waist'])
            bfNeck = int(form.cleaned_data['neck'])
            bfHip = int(form.cleaned_data['hips'])
            
            logH = math.log10(bfHeight)
            
            #163.205×log10(waist+hip-neck) - 97.684×(log10(height)) - 78.387
            
            if bfHip > 0:
                logWHN = math.log10(bfWaist+bfHip-bfNeck)
                result = 163.205*logWHN - 97.684*(logH) - 78.387
                bfResult = round(result, 2)
            else:
                logWN = math.log10(bfWaist - bfNeck)
                result = 86.010*logWN - 70.041*logH + 36.76
                bfResult = round(result, 2)
        
            print("Form valid")
        else:
            print("Form is not valid")
            print(form.errors)
            
        #handle update progress    
        progress_form = progress(request.POST)
        if progress_form.is_valid():
            print('Progress Valid')
            progress_form.save() #save to database
        else:
            print('Progress invalid')
            print(progress_form.errors)
        

        context = {'bfResult': bfResult, 'form': form, 'progress': progress_form}
        return render(request, 'fit/index.html', context)

    