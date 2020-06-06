to run locally, make sure flask is installed.


change into directory that this repo is located on your local machine.


In a terminal: (mac uses 'export', windows uses 'set') do the following two commands

$ export FLASK_APP=flaskAPP.py 

$ export FLASK_ENV=development

the last export allows flask to be ran in development mode. Some features of flask's development mode
are debugging features, and will automatically rerun when a source code change was made.

now you are ready to run flask with the command:

$ run flask


once started up, you can navigate to the webaddress and hit endpoints created in flaskAPI.py
