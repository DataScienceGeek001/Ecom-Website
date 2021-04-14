from django.shortcuts import render
from accounts.models import Newuser
from django.contrib import messages
# Create your views here.

def IndexPage(request):
    return render(request, 'index.html') 


def Userreg(request):
    if request.method == "POST":
        Username = request.POST['Username']
        Fullname = request.POST['Fullname']
        Email = request.POST['Email']
        Mobile = request.POST['Mobile']
        Pwd = request.POST['Password']

        Newuser(Username=Username, Fullname = Fullname, Email=Email, Mobile=Mobile, Pwd=Pwd).save()
        messages.success(request, 'The New User '+ request.POST['Username'] +' is saved Successfully...')
        return render(request, 'registration.html')
    
    else:
        return render(request, 'registration.html')


def loginpage(request):
    if request.method == "POST":
        try:
            Userdetails = Newuser.objects.get(Username=request.POST['Username'], Pwd=request.POST['Password'])
            print('Username = ', Userdetails)
            request.session['Username'] = Userdetails.Username
            return render(request, 'index.html')
        except Newuser.DoesNotExist as e:
            messages.success(request, 'Username / Password Invalid....!')
    
    return render(request, 'login.html')

def logout(request):
    try:
        del request.session['Username']
    except:
        return render(request, 'index.html')
    return render(request, 'index.html')