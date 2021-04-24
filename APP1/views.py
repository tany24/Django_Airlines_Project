from django.shortcuts import render
from django.http import HttpResponse
from APP1.models import AccessRecord, Topic, Webpage


# Create your views here.

#def index(request):
#    return HttpResponse("Good Morning !")

def originl_index(request):
    my_dict = {'insert_me':"Hello i am from the views.py -> index function ! <em>via the path -> templates/APP1/index.h</em>"}
    return render(request,'APP1/originl_index.html',context=my_dict)

#            New INDEX files

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,'APP1/index.html',context=date_dict)
#   my_dict = {'insert_me':"Hello i am from the views.py -> index function ! <em>via the path -> templates/APP1/index.h</em>"}
#   return render(request,'APP1/index.html',context=my_dict)

def help(request):
    helpdict = {'insertHELP':"THE HELP PAGE :\n Get help about issues here !"}
    return render(request,'APP1/help.html',context=helpdict)
