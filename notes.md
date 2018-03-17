# Get Python server running using these steps

1. Install python latest version globally using homebrew - homebrew install python
    a. python --version - checks python version

2. install virutalenvwrapper to set up an environment for django using the following link with the provided instruction
https://virtualenvwrapper.readthedocs.io/en/latest/

# Setting up environment for new app and the server

'pip install -r requirements.txt' - installs the dependences off of the requirement.txt file. Important for installing any needed dependencies. Similar to npm install to install required dependencies

'virtualenv env' - creates the env folder with all the necessary files to run a virtual environment

'django-admin startproject hello' - creates a new project called 'hello'

'. env/bin/activate' - activate the environment with activate as the key folder to start the virtual environment up

'pip install django' - now that you have set up and activated the environment, you can now easily install django into the environment context
    a. 'python -m django --version' - checks django version

'deactivate' - deactivates the virtual environment

'/manage.py runserver' - starts up the python/django based server. Make sure that the manage.py file can be found when typing 'ls' or 'dir' in the terminal before you start up server. Usually located in the main app folder itself
    * 'python manage.py runserver 0:8000' - you can specify port number like this by adding number at the end of command

'ctrl + c' - shuts down the server 

'https://docs.djangoproject.com/en/2.0/intro/tutorial01/' - example of a python app 

# App Set Up: part 2

'./manage.py startapp polls' - starts a new app called polls. Make sure to use this command when manage.py is there in the terminal location

* The include() function allows referencing other URLconfs. Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing. The idea behind include() is to make it easy to plug-and-play URLs. Since polls are in their own URLconf (polls/urls.py), they can be placed under “/polls/”, or under “/fun_polls/”, or under “/content/polls/”, or any other path root, and the app will still work.

* urls.py - contains the Routes that exists in your app

* views.py - contain the html that will be rendered on a particular route

* admin.py - allows apps to be displayed on the admin site. Otherwise, the app will not show up on the admin site. The admin website provides a user interface for non programmers to add functionality or make changes to database. 

* __init__.py - these files are to usually be kept empty as they auto generate. double underline indicates that they are system files

#. Databases in Python

* models.py - operates similarly to how models operate in mongoose where the model represents the structure for all data coming into the database

'./manage.py makemigrations polls' - makemigrations tells Django that you have made changes to your models and that you would like these changes stored as migrations

'./manage.py sqlmigrate polls 0001' - sqlmigrate command takes migration names and returns their SQL. It does not run the actual migration itself. Note that primary keys are added automatically and appends _id to the foreign key field name. 

'./manage.py check' - check for problems in your project without making migrations or touching the database.

'./manage.py migrate' - migrate takes all migrations that haven't been applied using a special table in your database called django_migrations and runs them against your database. It basically synchronize changes made in model with the schema in the database. At this point you are making a commit to the migrations made

# Using Python Shell for databases

'./manage.py shell' - starts up the python shell and test Django api. 

'from polls.models import Question, Choice' - Imports the model classes we just wrote

'Question.objects.all()' - returns all objects, instances of the type 'Question'
<QuerySet []>

'from django.utils import timezone' - imports the provided timezone from django itself

'q = Question(question_text="What's new?", pub_date=timezone.now())' - Create a new Question. Support for time zones is enabled in the default settings file, so Django expects a datetime with tzinfo for pub_date. Use timezone.now() instead of datetime.datetime.now() and it will do the right thing.

'q.save()' - Save the object into the database. You have to call save() explicitly.

'q.id' - # Now it has an ID. In this case, it will return 1.

'q.question_text' - Access model field values via Python attributes. Will return "What's new?" in this case

'q.question_text = "What's up?"' - Change values by changing the attributes, then calling save().
'q.save()' 

'Question.objects.all()' - objects.all() displays all the questions in the database.


# Creating a Admin User

* Run these commands on a terminal

'python manage.py createsuperuser' - creates a user who can login into the admin site

'Username: admin' enter desired username (use admin for now)

'Email address: youemailhere@example.com' - optional; Note you will also be asked to enter a password as well (use admin for now). Admin website can always be found on the server localhost/admin

# Python Authentication

* admin users - has built in authentication, has access permissions wth access to pretty much anything

* staff users - can mess with data but has limited permissions

'@login_required' checks if user is logged in before taking user to a view. If yes, user is directed to view. If not, user is redirected to the login page which has a default url which can be changed using a redirect_field_name

'user = User.objects.create_user('john','lennon@thebeatles.com', 'johnpassword')'- This is done in the python shell and it basically creates a user that can login. It is not a admin user. You do not have to call user.save() as it will save automaticcaly. You do need a user.save() if you to change the data

#OAuth

'django-allauth==0.35.0' - add oauthentication to the app using django allauth. Add this to the requirement.txt followed by a terminal command 'pip install -r requirements.txt'. 

'pip install django-allauth' - install all auth directly using pip

* After installing new frameworks, always go to the setting.py file in your app and add the new framework to the list of installed apps. 
INSTALLED_APPS = [
    'charactercreator',
    'armory',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # sites important for auth and deployment
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github'
]

* Getting All Auth working
    1. http://django-allauth.readthedocs.io/en/latest/installation.html#django - Gives more instruction for all auth installation

    2. Afterward, login to admin, go to sites and change domain name 'example.com' into the domain name which you can find by looking at your url. By default, it is either localhost or in most case 4 numbers separated by a period with most common being '127.0.0.1'. Set this as both the domain name and display name

    3. Go to your oauth provider and follow its instructions e.g https://developer.github.com/apps/building-oauth-apps/creating-an-oauth-app/ for Github

    4. Add the secret keys given by the Provider into your social account tab in the admin web page. 

'127.0.0.1' - default domain name 

# Other Debugging Stuff 

* delete db.sqlite3 if database is not synced with models and 'makemigrations' + 'migrate' command does not work. After deleting run 'makemigrations' + 'migrate' again.

# Api 

* Not just referring to software development but development in general. It is simply a well defined specification for its behavior and for what it exposes. This well defined specification allows software to be built on top of it in a predictable manner. We are building on top of the layers of api over the course of decades. Important to note that it is commomly used to refer to a back end server  that receives, stores, and manipulates data over the network. Api can be public or private, paid or free.

# REST
* Representational Safe Transfer - web servies providing interoperability or RESTful web services. Its concerned with different HTTP methods and requests made to the server including Create, read, update, and delete operations. The HTTP methods includes GET, PUT (replace), PATCH(update), POST(create), DELETE and is applied to some entity like a database, request data, etc. REST is also stateless which means the request doesn't depend on other context but the request itself. Get request also nullipotent or a safe method which means calling it twice produces no side effects.

* http://www.django-rest-framework.org/tutorial/quickstart/ - Provides good sample code to follow when setting up RESTful application with Django. Note that it uses django rest framework which can either be install through pip or adding it into requirements.txt.

'pip install djangorestframework' - install RESTful framework for Django directly through pip

'djangorestframework==3.7.7' - add this line to requirements.txt and then call 'pip install -r requirements.txt' with the environment active in terminal ('. env/bin/activate' activates environment')

# GraphQL 

* GraphQL is a query language for your api and a way to think querying data using a single api input. There is a single endpoint is queried and relatively simple using json. It works relatively well with the React ecosystem.

# environment variables 
* variable typically as PATH which are varaibles exposed to your OS. Usually used for either creating new environment, keeping secrets safe, deploying websites.

'export ENVIRONMENT_VARIABLE=value' sets the environment variable value

'echo $ENVIRONMENT_VARIABLE' returns the value of the environment variable

# Heroku Install

'brew install heroku/brew/heroku' - installs heroku on mac using brew. 

'heroku login' - login heroku

'heroky create appname' - creates app called appname

'heroku git:remote -a app-name' - switch from one app to another 

'git push heroku master' - launches and deloys the app. It also pushes any new changes you made to the app as well

'git push -am "comment"' - commits change you made to files for it to be push up to the master heroku branch

'heroku run python manage.py migrate' stores changes you have made in a migration. It needs to run for new projects and whenever the schema for database updates

'heroku run python manage.py createsuperuser' - creates a super user for the heroky app

'heroku run python manage.py dbshell' - start the postgresql shell

'heroky run pythong manage.py shell' - run the shell

'heroku ps:scale web=0 --app django-stuff' - stops deployment 

'heroku ps:scale web=1 --app django-stuff' - starts deployment back up

'heroku config:set DEBUG=TRUE' - works the admin on and the possible paths

'heroku run python manage.py loaddata rpg/testdata.json'



