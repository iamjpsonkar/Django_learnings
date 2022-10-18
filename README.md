# Virtual Envirnoment

## Create virtualenv using
It is better to create python virtual envirnoment, so that in future, the program/application can be executed without any external dependencies.
<pre>python -m venv mydjango</pre>

## Activate your virtualenv
To activate any virtual envirnonment below command can be used
<pre>source mydjango/Scripts/activate</pre>
After activating virtual envirnoment, we can install any python module inside it using pip
<pre>pip install django</pre>

## Deactivate your virtualenv
To deactivate any virtual envirnonment below command can be used
<pre>deactivate</pre>


# Django

## Django Project
In Django, Every thing is done under a project/directory which is managed by django itself. To create any django project below command is used
<pre>django-admin startproject first_project</pre>

<pre>
first_project/
    manage.py
    first_project/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
</pre>
These files are:

- The outer first_project/ root directory is a container for your project. Its name doesn’t matter to Django. You can rename it to anything you like.
- manage.py
: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.
- The inner first_project/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. first_project.urls).
- first_project/__init__.py: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.
- first_project/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
- first_project/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.
- first_project/asgi.py: An entry-point for ASGI-compatible web servers to serve your project. See How to deploy with ASGI for more details.
- first_project/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more detai

</pre>
As soon as our project is created, yo can verify your project and django in one go, using below commands
<pre>
cd first_project
python manage.py startserver
</pre>

**Copy url and goto your browser to verify its working or not**

## Django Apps

### Create Django App
Inside a django project, every subtask is added as an app. To create any app inside a django project use below commands
<pre>python manage.py startapp first_app</pre>
<pre>
first_app/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
</pre>

### Register your Django App
Once any app is created, it must needs to be registerd with djgo project, to do that, Open first_project/settings.py and add your app name in INSTALLED_APPS


## Adding Views in your app
views.py basically defines the view/look of the djago. Let's create a hellow world html view for our app

Add below lines inside first_app/views.py
```python
from django.http import HttpResponse
def index(request=None):
    return HttpResponse('<h1>Hello World!!!</h1>')
```

Add below lines inside first_project/urls.py
```python
from first_app import views
# in urlpatterns add below lines
path('/',views.index,name='index'),
```
**Save and rerun your server to get your app output**

In a django project, there can be multiple apps, to mange there routing we can define a seperate urls.py for each app, and then we can include that urls.py in our main project.

Copy first_project/urls.py to first_app/urls.py and replace all content of urlpatterns with
```python
path('/',views.index,name='index')
```
Now, inside first_project/urls.py add below lines
```python
from django.urls import include
# in urlpatterns add below lines
path('first_app/',include("first_app.urls"))
```

**Save everything and rerun your server, copy url 127.0.0.1:8000/first_app/ to see the output**

## Django Templates
In views.py we can define functions for difeerent views, but  for bigger apps, we need big html output, and returning/manageing such complex html string though the functions of views.py, is very tidius. These large htmls strings can be handled using templets.

Templates are basically html files that can be retured by django view functions as a view.

In Django, youcan have templates at two levels
- Project Level Templates:
Template directory is created inside main djago project and it is shared by all other apps. This is helpfull, when you have very few apps, and size of your project is very small.
- App Level Templates:
Template directory is created separately for each application. This is helpfull, when you have multiple apps, and size of your project is very large.

### Project Level Templates
Create templates directory inside your django project, and create same structure inside templates directory as your django project and app structure is.
<pre>
first_project/
    templates/
        first_app/
            index.html
</pre>
        
Now add your code in new index.html.

Adding templates in settings.py

open first_project/first_project/settings.py, add below lines ,after BASE_DIR defination
</pre>
```python
import os
TEMPLATES_DIR = os.path.join(BASE_DIR,"templates")
# find TEMPLATE variable and add below value in DIR
TEMPLATES_DIR,
```

Now, open first_app/views.py and add below lines

```python
from django.shortcuts import render
# change defination of index function
def index(request=None):
    return render(request,'first_app/index.html')
```
**Save everything and rerun server to see your output**

### App Level Templates

**To be completed**


## Django Static files
Any web developement project have some more type of files other then html files, these other files are known as static files.
Like for html we have TEMPLATES, for other files such as images, css and javascript we have STATIC
We can have two levels of static files
- Project level Static Files
- App level Static files

### Project Level Static Files
Create below directory structure
<pre>
first_project/
    static/
        images/
        css/
        javascript/
</pre>

Now in first_project/first_project/settings.py, add below lines after the defination of TEMPLATES_DIR
</pre>
```python
STATIC_DIR = os.path.join(BASE_DIR,"static")
# scrolldown to STATIC_URL in settings.py
# add below lines
STATICFILES_DIR=[
    STATIC_DIR,
    ]
```

Now in index.html, add below lines after <!Doctype>

```html
{% load static %}
<!-- in head add below line -->
<link href="{% static 'css/mycss.css' %}" rel="stylesheet">
<!-- in body add below lines -->
<h3>Django Image</h3>
<img src="{% static 'images/DjangoFeaturedImage.jpeg' %}" alt="Image Not Found!!!" width="600px" height="400px"/>
```
**Save everything and rerun server to see output**

### App Level Static Files

**To be completed**


## Django Models
Almost every web application, works/manage on Data. These Data are stored in Databases, in the form of tables. 
- Handling of these type of data, is known as Backend.
- Handling of HTML and views is Frontend.

To communicate with data stored in databases, we use database languages, such as SQL, NO-SQL.

Complex queries are written and executed to manage data stored in the databases.

Django provides a functionality named **Model**, that can help us to avoid these extra complex querries, to handle such data.

Structure of table can be defined as a class, these classed inherit Model class of django. After **Migration**, all these models are converted into tables.

### Creating Models
Inside your app, there is a models.py, add below lines of code to models.py
```python
class Topic(models.Model):
    top_name=models.CharField(max_length=264,unique=True)
    
    def __str__(self):
        return self.top_name
```

The above class, after migrating will create below  **Topic table**

| top_name |
|----------|
| Topic-1  |
| Topic-2  |

In the same way, other tables can be created using Models

### Migrations
This basically saves/create our model for django

For migrations execute below commands
<pre>
python manage.py migrate
python manage.py makemigrations first_app
python manage.py migrate
</pre>

### Verify Migrations
Use python command line to check the migrations
```python
> python manage.py shell
>>> from first_app.models import Topic
>>> print(Topic.objects.all())
<QuerySet []>
>>> t=Topic(top_name="Social Network")
>>> t.save()
>>> print(Topic.objects.all())
<QuerySet [<Topic: Social Network>]>
>>> exit()
```

### Register Model
Newly created models, needs to be registered with django.

To register, newly created models, open first_app/admin.py and add below lines
```python
from first_app.models import Topic,Webpage,AccessRecord
admin.site.register(Topic)
```

### Superuser for admin
Execute below command to create superuser for django admin
<pre>python manage.py createsuperuser</pre>

Now login to admin portal i.e. http://127.0.0.1:8000/admin
