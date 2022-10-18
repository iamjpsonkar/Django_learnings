# Create virtualenv using
> virtualenv mydjango

## Activate your virtualenv using
>source mydjango/Scripts/activate

## Install django using
> pip install django

# Create your first project using
> django-admin startproject first_project

# Run your project and server
> cd first_project

> python manage.py startserver

**Copy url and goto your browser to verify its working or not**

# Create your first app
> python manage.py startapp first_app

# Register your app
<pre>
open first_project/settings.py
add your app name in INSTALLED_APPS
</pre>

# Code your app
<pre>
open first_app/views.py
add below lines
</pre>
```python
from django.http import HttpResponse
def index(request=None):
    return HttpResponse('<h1>Hello World!!!</h1>')
```
<pre>
open first_project/urls.py
add below lines
</pre>
```python
from first_app import views
# in urlpatterns add below lines
path('/',views.index,name='index'),
```
**Save and rerun your server to get your app output**

<hr/>

## Using include()
<pre>
open first_project/urls.py
add below lines
</pre>

```python
from django.urls import include
# in urlpatterns add below lines
path('first_app/',include("first_app.urls"))
```
<pre>
now create first_app/urls.py
copy content from first_project/urls.py to first_app/urls.py
remove all content of urlpatterns
add below lines
</pre>

```python
path('/',views.index,name='index')
```

<pre>
Save everything and rerun your server
copy url 127.0.0.1:8000/first_app/
see your app output
</pre>

# Using Templates
<pre>
Create first_project/templates/first_app/index.html
add your code in new index.html
open first_project/first_project/settings.py
add below lines ,after BASE_DIR defination
</pre>
```python
import os
TEMPLATES_DIR = os.path.join(BASE_DIR,"templates")
# find TEMPLATE variable and add below value in DIR
TEMPLATES_DIR,
```
<pre>
Open first_app/views.py
add below lines
</pre>
```python
from django.shortcuts import render
# change defination of index function
def index(request=None):
    my_dict={'myname':'Jay Prakash Sonkar'}
    return render(request,'first_app/index.html',context=my_dict)
```
**Save everything and rerun server to see your output**

# Adding static files
<pre>
Create first_project/static directory
Create below directories inside static directory

- images
- css
- javascript

Open first_project/first_project/settings.py
add below lines below TEMPLATES_DIR
</pre>
```python
STATIC_DIR = os.path.join(BASE_DIR,"static")
# scrolldown to STATIC_URL in settings.py
# add below lines
STATICFILES_DIR=[
    STATIC_DIR,
    ]
```
<pre>
Open index.html
add below lines after <!Doctype>
</pre>
```html
{% load static %}
<!-- in head add below line -->
<link href="{% static 'css/mycss.css' %}" rel="stylesheet">
<!-- in body add below lines -->
<h3>Django Image</h3>
<img src="{% static 'images/DjangoFeaturedImage.jpeg' %}" alt="Image Not Found!!!" width="600px" height="400px"/>
```
**Save everything and rerun server to see output**