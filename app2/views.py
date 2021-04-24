from django.shortcuts import render
from django.http import HttpResponse
from app2.models import UserInfo

# Create your views here.

def userList(request):
    users = UserInfo.objects.order_by('first_name')
    userListDict = {'user_info':users}
    return render(request,'app2/userList.html',context=userListDict)
