# Get Python server running using these steps

1. Install python latest version globally using homebrew - homebrew install python
    a. python --version - checks python version

2. install virutalenvwrapper using the following link with the provided instruction
https://virtualenvwrapper.readthedocs.io/en/latest/

3. setting up a new app:

'pip install -r requirements.txt' - installs the dependences off of the requirement.txt file. Important for installing any needed dependencies. Similar to npm install to install required dependencies

'virtualenv env' - creates the env folder with all the necessary files to run a virtual environment

'django-admin startproject hello' - creates a new project 

'. env/bin/activate' - activate the environment with activate as the key folder to start the virtual environment up

'pip install django' - now that you have set up and activated the environment, you can now easily install django into the environment context
    a. $ python -m django --version - checks django version

'deactivate' - deactivates the virtual environment

'python hello/manage.py runserver' - starts up the python/django based server
    * python manage.py runserver 0:8000 - you can specify port number like this by adding number at the end of command

'ctrl + c' - shuts down the server 

'https://docs.djangoproject.com/en/2.0/intro/tutorial01/' - example of a python app 

4. app set up p2.

'$ python manage.py startapp polls' - starts a new app called polls. Make sure to use this command when manage.py is there in the terminal location

* The include() function allows referencing other URLconfs. Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing. The idea behind include() is to make it easy to plug-and-play URLs. Since polls are in their own URLconf (polls/urls.py), they can be placed under “/polls/”, or under “/fun_polls/”, or under “/content/polls/”, or any other path root, and the app will still work.

* urls.py - contains the Routes that exists in your app

* views.py - contain the html that will be rendered on a particular route

* admin.py - allows apps to be displayed on the admin site. Otherwise, the app will not show up on the admin site. The admin website provides a user interface for non programmers to add functionality or make changes to database. 

* __init__.py - these files are to usually be kept empty as they auto generate. double underline indicates that they are system files

5. Databases in Python

* models.py - operates similarly to how models operate in mongoose where the model represents the structure for all data coming into the database

'python manage.py makemigrations polls' - makemigrations tells Django that you have made changes to your models and that you would like these changes stored as migrations

'python manage.py sqlmigrate polls 0001' - sqlmigrate command takes migration names and returns their SQL. It does not run the actual migration itself. Note that primary keys are added automatically and appends _id to the foreign key field name. 

'python manage.py check' - check for problems in your project without making migrations or touching the database.

'python manage.py migrate' - migrate takes all migrations that haven't been applied using a special table in your database called django_migrations and runs them against your database. It basically synchronize changes made in model with the schema in the database. At this point you are making a commit to the migrations made

'python manage.py shell' - starts up the python shell and test Django api. 

>>> from polls.models import Question, Choice   # Import the model classes we just wrote.

# No questions are in the system yet.
>>> Question.objects.all()
<QuerySet []>

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
>>> q.save()

# Now it has an ID.
>>> q.id
1

# Access model field values via Python attributes.
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

# Change values by changing the attributes, then calling save().
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() displays all the questions in the database.
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>

6. Creating a Admin User

* Run these commands on a terminal

'python manage.py createsuperuser' - creates a user who can login into the admin site

'Username: admin' enter desired username (use admin for now)

'Email address: youemailhere@example.com' - optional; Note you will also be asked to enter a password as well (use admin for now). Admin website can always be found on the server localhost/admin

