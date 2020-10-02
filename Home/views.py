from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

#win32bitcomapple

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/teacherlogin")

    else:
        return render(request, 'index.html')
    # return HttpResponse("Nice")

def quotes(request):
    return render(request, 'quotes.html')

def TeacherLogin(request):
    if request.method == "POST":
        teachername = request.POST.get('teachername')
        password = request.POST.get('password')
        user = authenticate(username=teachername, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')
 
def TeacherLogout(request):
    logout(request)
    return redirect("/teacherlogin")
 