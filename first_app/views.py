from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request=None):
    my_dict={'myname':'Jay Prakash Sonkar'}
    return render(request,'first_app/index.html',context=my_dict)