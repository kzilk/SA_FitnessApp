from django.shortcuts import render, redirect
from django.views import View
from .forms import bfCalcForm, progressForm, liftForm, routineForm, targetForm, recipeForm
from .models import progressModel, liftModel, recipeModel
import math
    
class Index(View):
    def get(self, request):

        form = bfCalcForm()
        weightProg = progressForm()
        liftProg = liftForm()
        routineRec = routineForm()
        targetRec = targetForm()
        recipeRec = recipeForm()


        weight_data = progressModel.objects.all()

        lift_data = liftModel.objects.all()
       
        recipe_data = recipeModel.objects.all()

        context = {'form':form, 'progress':weightProg, 'lifts':liftProg,
                   'weight_data':weight_data, 'lift_data':lift_data, 'routineRec':routineRec,
                   'targetRec':targetRec, 'recipeRec':recipeRec, 'recipe_data':recipe_data}
        return render(request, 'fit/index.html', context) 
   
    def post(self, request):
        bfResult = None
        form = bfCalcForm()
        
        progress_form = progressForm()
        lift_form = liftForm()
        
        routineRec = routineForm()
        routine_selection = None
        
        targetRec = targetForm()
        target_selection = None

        if 'bfButton' in request.POST:
            form = bfCalcForm(request.POST)
            if form.is_valid():
                # process bfCalc data and perform calculations
                bfHeight = int(form.cleaned_data['height'])
                bfWaist = int(form.cleaned_data['waist'])
                bfNeck = int(form.cleaned_data['neck'])
                bfHip = int(form.cleaned_data['hips'])

                logH = math.log10(bfHeight)

                if bfHip > 0:
                    logWHN = math.log10(bfWaist + bfHip - bfNeck)
                    result = 163.205 * logWHN - 97.684 * (logH) - 78.387
                    bfResult = round(result, 2)
                else:
                    logWN = math.log10(bfWaist - bfNeck)
                    result = 86.010 * logWN - 70.041 * logH + 36.76
                    bfResult = round(result, 2)
            else:
                print("Form is not valid")
                print(form.errors)

        elif 'weightButton' in request.POST:
            # handle update weight progress
            progress_form = progressForm(request.POST)
            if progress_form.is_valid():
                print('Progress Valid')
                progress_form.save()  # save to database
                return redirect(request.path) #refresh page to view updated table
            else:
                print('Progress invalid')
                print(progress_form.errors)

        elif 'liftButton' in request.POST:
            # handle update lift progress
            lift_form = liftForm(request.POST)
            if lift_form.is_valid():
                print('lift valid')
                lift_form.save()
                return redirect(request.path) #refresh page to view updated table
            else:
                print('Lift invalid')
                print(lift_form.errors)

        elif 'routineButton' in request.POST:
            # handle routine selection
            routineRec = routineForm(request.POST)
            if routineRec.is_valid():
                routine_selection = routineRec.cleaned_data['routine_choice']
            else:
                print('Routine invalid')
                print(routineRec.errors)
            
        elif 'targetButton' in request.POST:
            # handle targeting muscle group
            targetRec = targetForm(request.POST)
            if targetRec.is_valid():
                target_selection = targetRec.cleaned_data['target_choice']
            else:
                print('Target invalid')
                print(targetRec.errors)

        weight_data = progressModel.objects.all()
        lift_data = liftModel.objects.all()
        recipe_data = recipeModel.objects.all()
        
        context = {'bfResult': bfResult, 
                   'form': form, 
                   'progress': progress_form, 
                   'weight_data': weight_data,
                   'lifts': lift_form,
                   'lift_data': lift_data,
                   'routineRec': routineRec, 
                   'routine_selection': routine_selection, 
                   'targetRec': targetRec,
                   'target_selection': target_selection,
                   'recipe_data': recipe_data}
                    
        return render(request, 'fit/index.html', context)