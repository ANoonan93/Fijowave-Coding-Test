AUTHOR: ADAM NOONAN
DATE: 10/1/2017
TITLE: FIJOWAVE CODE TEST README

APP STRUCTURE:

The src file contains all aspects of the web app. This includes the mysite, polls, 
staticfiles, templates folders, sqlite file and manage.py. 

The mysite folder contains the settings, wsgi, urls and __init__ py files.

The polls folder contains the files that make up the main app unique to this web app. 
These are the views, models, tests, apps, admin and __init__ py files. The migrations
folder is also within this polls folder. It contains information on Django model 
migrations to the database.

The staticfiles folder contains files that are used directly by the web app or uploaded by users.
Two folders, admin and flot. Both contain javascript files that can be used in the Django template files.

The templates folder holds the various django template.py files used for html/css purposes.

 


 