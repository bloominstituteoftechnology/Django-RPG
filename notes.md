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

# App Set up: part 2

'$ python manage.py startapp polls' - starts a new app called polls. Make sure to use this command when manage.py is there in the terminal location

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

'user = User.objects.create_user('john','lennon@thebeatles.com', 'johnpassword')' creates a user that can login. It is not a admin user. You do not have to call user.save() as it will save automaticcaly. You do need a user.save() if you to change the data

# Other Debugging Stuff 

* delete db.sqlite3 if database is not synced with models and 'makemigrations' + 'migrate' command does not work. After deleting run 'makemigrations' + 'migrate' again.

# Api 

* Not just referring to software development but development in general. It is simply a well defined specification for its behavior and for what it exposes. This well defined specification allows software to be built on top of it in a predictable manner. We are building on top of the layers of api over the course of decades. Important to note that it is commomly used to refer to a back end server  that receives, stores, and manipulates data over the network. Api can be public or private, paid or free.

# REST
* Representational Safe Transfer - web servies providing interoperability or RESTful web services. Its concerned with different HTTP methods and requests made to the server including Create, read, update, and delete operations. The HTTP methods includes GET, PUT (replace), PATCH(update), POST(create), DELETE and is applied to some entity like a database, request data, etc. REST is also stateless which means the request doesn't depend on other context but the request itself. Get request also nullipotent or a safe method which means calling it twice produces no side effects.