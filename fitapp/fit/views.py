from django.shortcuts import render, redirect
from django.views import View
from .forms import bfCalcForm, progressForm, liftForm
from .models import progressModel, liftModel
import math
    
class Index(View):
    def get(self, request):
        form = bfCalcForm()
        weightProg = progressForm()
        liftProg = liftForm()
        weight_data = progressModel.objects.all()
        print(weight_data)
        lift_data = liftModel.objects.all()
        print(lift_data)
        context = {'form':form, 'progress':weightProg, 'lifts':liftProg, 'weight_data':weight_data, 'lift_data':lift_data}       
        return render(request, 'fit/index.html', context) 
   
    def post(self, request): 
        bfResult = None
        
        form = bfCalcForm(request.POST)
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
            
       
        #handle update weight progress    
        progress_form = progressForm(request.POST)
        if progress_form.is_valid():
            print('Progress Valid')
            progress_form.save() #save to database
            return redirect(request.path)
        else:
            print('Progress invalid')
            print(progress_form.errors)
            
        #handle update lift progress
        lift_form = liftForm(request.POST)
        if lift_form.is_valid():
            print('lift valid')
            lift_form.save()
            return redirect(request.path)
        else:
            print('Lift invalid')
            print(lift_form.errors)
    

        context = {'bfResult': bfResult, 'form': form, 'progress': progress_form, 'lifts': lift_form}
        return render(request, 'fit/index.html', context)