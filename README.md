to run locally, make sure flask is installed.
    change into directory that this repo is located on your local machine.

    to run simlpy type 'python3 main.py' into the terminal to get you going

    OR
        In a terminal: (mac uses 'export', windows uses 'set') do the following two commands

        $ export FLASK_APP=flaskAPI.py

        $ export FLASK_ENV=development

        the last export allows flask to be ran in development mode. Some features of flask's development mode
        are debugging features, and will automatically rerun when a source code change was made.

        now you are ready to run flask with the command:

        $ flask run


    once started up, you can navigate to the webaddress and hit endpoints created in main.py


To run in gcloud App Engine
    make sure the gcloud SDK is installed on your machine.

    navigate to the main directory (flask_api):
        $ gcloud deploy app app.yaml
        
    this will deploy your app into GCP App Engine (assuming you have a project created
        and are logged in on your machine)

    extra helpful gcloud commands:
        You can stream logs from the command line by running:
        $ gcloud app logs tail -s default

        To view your application in the web browser run:
        $ gcloud app browse
