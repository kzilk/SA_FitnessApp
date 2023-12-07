# SA_FitnessApp
This is an application that can be used by an individual to track their progress when it comes to fitness and training, current description and details are based on the current incomplete application.

As a note, in it's current iteration, the page will state sections you are not yet using have required inputs needed, and when inputting progress, the page will load a blank table. Reloading the page or resbumitting corrects the table to show all entries

REQUIREMENTS
  Django and Python
    https://docs.djangoproject.com/en/4.2/intro/install/

TO USE
  After downloading the main file, open your terminal or command prompt and change the directory to the 'fitapp' folder.
    Enter the following one at a time, pressing enter once done with each line. This will create the connected databases to store your saved data
        python manage.py makemigrations
        python manage.py migrate

  To run the program
    python manage.py runserver

  Now, in your browser, enter '127.0.0.1:8000' in the url, this should load a page with three features so far: a body fat calculator, an input method to store your weight progress, and a table showing only the headers ID, date, bf, and weight.

  Body Fat Calculator
    To use, enter in your measurments for the relavent parts in inches, as the header says, the hip entry is for women only and should be entered as '0' if you are a man.
    Once filled, click 'Calculate' and your body fat percentage will be displayed. Note, it will state that the fields under Progress Input are required but this may be disregarded.
    

  Progress Input
    Here, you enter your bodyfat percentage which you can get from the above function and your current weight. Once done, click 'Save' and the page will load a blank table, regardless of other entries, and ask for required inputs under the BF Calculator entry. Please reenter the URL '127.0.0.1:8000' and it will be displayed in full.
        NOTE: do not refresh the page as that will resubmit the form resulting in duplicate entries

  Table
    This table will load automatically with the data you inputed in the previous section. the id is auto-created as a way to give each entry a unique identifier and the date is automatically set based on when you save your input. 



TO BE CORRECTED
  First correction point is to not require entries on sections not currently used, and not require resetting the page to view new table entries. 

TO BE ADDED
  Additional input section and table to track lifting performances. Current table may be updated to include these markers or a new one may be entered below

  Drop down menus to select training level eg novice, beginner, intermidiate etc, selection would return a suggested weightlifting routine for that level

  Drop down menu to select body part/region eg legs, arms, back, with possibly more specific parts to then return specified exercises, stretches, and form recommendations to improve or help recover training

  PreSet table with descriptions of recipes including macros, calories, and links to the websites showing them
