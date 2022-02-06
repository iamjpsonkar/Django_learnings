from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request=None):
    my_dict={'myname':'Jay Prakash Sonkar'}
    return render(request,'first_app/index.html',context=my_dict)

def data_index(request=None):
    webpage_list=AccessRecord.objects.order_by('date')
    date_dict={'access_record':webpage_list}
    return render(request,'first_app/data_index.html',context=date_dict)
    