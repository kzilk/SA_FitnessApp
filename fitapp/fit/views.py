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
        print(weight_data)

        lift_data = liftModel.objects.all()
        print(lift_data)

        recipe_data = recipeModel.objects.all()
        print(recipe_data)

        context = {'form':form, 'progress':weightProg, 'lifts':liftProg,
                   'weight_data':weight_data, 'lift_data':lift_data, 'routineRec':routineRec,
                   'targetRec':targetRec, 'recipeRec':recipeRec, 'recipe_data':recipe_data}
        return render(request, 'fit/index.html', context) 
   
    def post(self, request):
        bfResult = None

        form = bfCalcForm(request.POST)
        if form.is_valid():
            # process bfCalc data and perform calculations
            bfHeight = int(form.cleaned_data['height'])
            bfWaist = int(form.cleaned_data['waist'])
            bfNeck = int(form.cleaned_data['neck'])
            bfHip = int(form.cleaned_data['hips'])

            logH = math.log10(bfHeight)

            # 163.205×log10(waist+hip-neck) - 97.684×(log10(height)) - 78.387

            if bfHip > 0:
                logWHN = math.log10(bfWaist + bfHip - bfNeck)
                result = 163.205 * logWHN - 97.684 * (logH) - 78.387
                bfResult = round(result, 2)
            else:
                logWN = math.log10(bfWaist - bfNeck)
                result = 86.010 * logWN - 70.041 * logH + 36.76
                bfResult = round(result, 2)

            print("Form valid")
        else:
            print("Form is not valid")
            print(form.errors)

        # handle update weight progress
        progress_form = progressForm(request.POST)
        if progress_form.is_valid():
            print('Progress Valid')
            progress_form.save()  # save to database
            return redirect(request.path) #refresh page to view updated table
        else:
            print('Progress invalid')
            print(progress_form.errors)

        # handle update lift progress
        lift_form = liftForm(request.POST)
        if lift_form.is_valid():
            print('lift valid')
            lift_form.save()
            return redirect(request.path) #refresh page to view updated table
        else:
            print('Lift invalid')
            print(lift_form.errors)

        # handle routine selection
        routineRec = routineForm(request.POST)
        routine_selection = None
        if routineRec.is_valid():
            routine_selection = routineRec.cleaned_data['routine_choice']
        else:
            print('Routine invalid')
            print(routineRec.errors)
            

        # handle targeting muscle group
        targetRec = targetForm(request.POST)
        target_selection = None
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
                   'lifts': lift_form,
                   'routine': routineRec, 
                   'routine_selection': routine_selection, 
                   'targetRec': targetRec,
                   'target_selection': target_selection,
                   'weight_data': weight_data,
                   'lift_data': lift_data,
                   'recipe_data': recipe_data}
                    
        return render(request, 'fit/index.html', context)