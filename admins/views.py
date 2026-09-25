from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from users.models import UserRegistrationModel


def AdminLogin(request):
    return render(request,'AdminLogin.html',{})

def AdminHome(request):
    return render(request, 'admins/AdminHome.html')


def AdminLoginCheck(request):
    if request.method == 'POST':
        usrid = request.POST.get('loginname')
        pswd = request.POST.get('pswd')
        print("User ID is = ", usrid)
        if usrid == 'admin' and pswd == 'admin':
            return render(request, 'admins/AdminHome.html')

        else:
            messages.success(request, 'Please Check Your Login Details')
    return render(request, 'AdminLogin.html',{})


def RegisterUsersView(request):
    data = UserRegistrationModel.objects.all()
    return render(request,'admins/ViewRegisterUsers.html',{'data':data})


def ActivaUsers(request):
    if request.method == 'GET':
        id = request.GET.get('uid')
        status = 'activated'
        print("PID = ", id, status)
        UserRegistrationModel.objects.filter(id=id).update(status=status)
        data = UserRegistrationModel.objects.all()
        return render(request,'admins/ViewRegisterUsers.html',{'data':data})