from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord, User
from . import forms
from first_app.forms import NewUserForm



# Create your views here.
def index(request=None):
    my_dict={'myname':'Jay Prakash Sonkar','text':"I am Text.",'number':1000}
    return render(request,'first_app/index.html',context=my_dict)

def data_index(request=None):
    webpage_list=AccessRecord.objects.order_by('date')
    date_dict={'access_record':webpage_list}
    return render(request,'first_app/data_index.html',context=date_dict)
    
def user_index(request=None):
    user_list=User.objects.values()
    user_dict={
        'user_data':user_list
    }
    return render(request,'first_app/user_index.html',context=user_dict)

def form_name_view(request):
    form=forms.FormName()
    
    if request.method=='POST':
        form=forms.FormName(request.POST)
        
        if form.is_valid():
            print("Validation Success!!!")
            print("Name:  ",form.cleaned_data['name'])
            print("Email: ",form.cleaned_data['email'])
            print("Text:  ",form.cleaned_data['text'])
            
    return render(request,'first_app/basicform.html',context={'form':form})


def signup_user(request):
    form=NewUserForm()
    
    if request.method=='POST':
        form=NewUserForm(request.POST) 
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Form Invalid!!!")
            
    return render(request,'first_app/signup.html',{'form':form})    

def relative_url(request):
    return render(request,'first_app/relative_url.html')

def other_page(request):
    return render(request,'first_app/otherpage.html')