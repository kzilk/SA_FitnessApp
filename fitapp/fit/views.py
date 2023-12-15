from django.shortcuts import render, redirect
from django.views import View
from .forms import bfCalcForm, weightForm, liftForm, routineForm, targetForm, recipeForm
from .models import weightModel, liftModel, recipeModel
import math
    
class Index(View):
    def get(self, request):
        
        #set forms to variables to load context
        bfForm = bfCalcForm()
        weightProg = weightForm()
        liftProg = liftForm()
        routineRec = routineForm()
        targetRec = targetForm()
        recipeRec = recipeForm()

        #set objects in models from tables as variables to ensure stored data is printed
        weight_data = weightModel.objects.all()
        lift_data = liftModel.objects.all()
        recipe_data = recipeModel.objects.all()

        #set context for data to load
        context = {'bfForm':bfForm, 
                   'weight':weightProg, 
                   'weight_data':weight_data, 
                   'lifts':liftProg,
                   'lift_data':lift_data, 
                   'routineRec':routineRec,
                   'targetRec':targetRec, 
                   'recipeRec':recipeRec, 
                   'recipe_data':recipe_data}
        
        #return on screen at path, shows when first loading page
        return render(request,'fit/index.html', context) 
   
    def post(self, request):
        #initialize bodyfat data
        bfResult = None
        bfForm = bfCalcForm()
        
        #initialize chart data
        weight_form = weightForm()
        lift_form = liftForm()
        
        #initialize routine data
        routineRec = routineForm()
        routine_selection = None
        
        #initialize routine data
        targetRec = targetForm()
        target_selection = None

        #check which button was pressed:
        if 'bfButton' in request.POST:
            bfForm = bfCalcForm(request.POST)
            #run bodyfat calucations and validation if button pressed
            if bfForm.is_valid():
                # process bfCalc data and perform calculations
                bfHeight = int(bfForm.cleaned_data['height'])
                bfWaist = int(bfForm.cleaned_data['waist'])
                bfNeck = int(bfForm.cleaned_data['neck'])
                bfHip = int(bfForm.cleaned_data['hips'])

                logH = math.log10(bfHeight)

                #check if hip entry for male or female, run appropriate calculation
                if bfHip > 0:
                    logWHN = math.log10(bfWaist + bfHip - bfNeck)
                    result = 163.205 * logWHN - 97.684 * (logH) - 78.387
                    bfResult = round(result, 2)
                else:
                    logWN = math.log10(bfWaist - bfNeck)
                    result = 86.010 * logWN - 70.041 * logH + 36.76
                    bfResult = round(result, 2)
            else:
                print("Bodyfat form is not valid")
                print(bfForm.errors)

        elif 'weightButton' in request.POST:
            # check if weight table input button pressed, save data to table if good entry
            weight_form = weightForm(request.POST)
            if weight_form.is_valid():
                weight_form.save()  # save to database
            else:
                print('Weight entry invalid')
                print(weight_form.errors)

        elif 'liftButton' in request.POST:
            # check if lift table input button pressed, save data to table if good entry
            lift_form = liftForm(request.POST)
            if lift_form.is_valid():
                print('lift valid')
                lift_form.save()
            else:
                print('Lift invalid')
                print(lift_form.errors)

        elif 'routineButton' in request.POST:
            # check which routine seletect and display
            routineRec = routineForm(request.POST)
            if routineRec.is_valid():
                routine_selection = routineRec.cleaned_data['routine_choice']
            else:
                print('Routine invalid')
                print(routineRec.errors)
            
        elif 'targetButton' in request.POST:
            # check which muscle group selected and display
            targetRec = targetForm(request.POST)
            if targetRec.is_valid():
                target_selection = targetRec.cleaned_data['target_choice']
            else:
                print('Target invalid')
                print(targetRec.errors)

        #set table values from models for context, place here so any updates above are read
        weight_data = weightModel.objects.all()
        lift_data = liftModel.objects.all()
        recipe_data = recipeModel.objects.all()
        
        #set context again with new potential return data, need all points to ensure specific return is used
        context = {'bfResult': bfResult, 
                   'bfForm': bfForm, 
                   'weight': weight_form, 
                   'weight_data': weight_data,
                   'lifts': lift_form,
                   'lift_data': lift_data,
                   'routineRec': routineRec, 
                   'routine_selection': routine_selection, 
                   'targetRec': targetRec,
                   'target_selection': target_selection,
                   'recipe_data': recipe_data}
                    
        #show on screen, now includes return data and happens after selection is made
        return render(request, 'fit/index.html', context)