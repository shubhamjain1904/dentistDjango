from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.template.loader import get_template
from django.template import Context
from .models import Post


# Create your views here.




def index(request):
    return render(request, 'index.html', {'title':'index'})

def home(request):
    return render(request,'home.html',{})

def contact(request):
    return render(request,'contact.html',{})

def pricing(request):
    return render(request,'pricing.html',{})

def services(request):
    return render(request,'services.html',{})

def openinghour(request):
    return render(request,'openinghour.html',{})

def about(request):
    return render(request,'about.html',{})


def report(request):
    return render(request,'report.html',{})



########### register here #####################################
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            ######################### mail system ####################################

            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form, 'title':'reqister here'})

################ login forms###################################################
def Login(request):
    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)

            return redirect('home')

        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form, 'title':'log in'})
def logout(request):
    return redirect('home')
