# SA_FitnessApp
This is an application that can be used by an individual to track their progress when it comes to fitness and training, current description and details are based on the current incomplete application.

REQUIREMENTS
  Django and Python:
    https://docs.djangoproject.com/en/4.2/intro/install/

TO USE:
  After downloading the main file, open your terminal or command prompt and change the directory to the 'fitapp' folder.
    Enter the following one at a time, pressing enter once done with each line. This will create the connected databases to store your saved data:
        python manage.py makemigrations //
        python manage.py migrate

  To run the program
   //linux: python3 manage.py runserver  //windows: py manage.py runserver

  Now, in your browser, enter '127.0.0.1:8000' in the url, this should load a page with three features so far: a body fat calculator, an input method to store your weight progress, and a table showing only the headers ID, date, bf, and weight.

  Body Fat Calculator: 
    To use, enter in your measurments for the relavent parts in inches, leaving the 'Hips' section at 0 if male as instructed.
    Once filled, click 'Calculate' and your body fat percentage will be displayed.
    

  Weight Progress Input: 
    Here, you enter your bodyfat percentage which you can get from the above function and your current weight. Once done, click 'Save' and the page will load the new entry to the table below

  Lift Progress Input:
    Similarly, here you enter your personal best lifts for each of these compound movements. You only need to enter one for it be be updated to the table, but you can fill out as many as have been accomplished. Once done, click 'Save' and the page will load the new entry to the table below


TO BE CORRECTED: removal or skipping of the 'id' column in each table

TO BE ADDED:
  Drop down menus to select training level eg novice, beginner, intermidiate etc, selection would return a suggested weightlifting routine for that level//

  Drop down menu to select body part/region eg legs, arms, back, with possibly more specific parts to then return specified exercises, stretches, and form recommendations to improve or help recover training//

  PreSet table with descriptions of recipes including macros, calories, and links to the websites showing them
