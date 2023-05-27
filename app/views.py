from django.shortcuts import render, redirect

# Forms
from .forms import CreateUserForm
from django.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#

from .models import Database

# Create your views here.


@login_required(login_url='login')
def home(request):
    return render(request, 'index.html')


@login_required(login_url='login')
def createProfile(request):

    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneNumber = request.POST.get('phoneNumber')
        linkedIn = request.POST.get('linkedIn')
        github = request.POST.get('github')
        resume = request.FILES.get('resume')
        instagram = request.POST.get('instagram')
        facebook = request.POST.get('facebook')
        resumeFileName = request.POST.get('resumeFileName')

        database = Database(
            user=user,
            name=name,
            email=email,
            phoneNumber=phoneNumber,
            linkedIn=linkedIn,
            github=github,
            resume=resume,
            instagram=instagram,
            facebook=facebook,
            resumeFileName=resumeFileName
        )
        database.save()

    return render(request, 'createProfile.html')


@login_required(login_url='login')
def editProfile(request):
    return render(request, 'editProfile.html')


# ############################## LOGIN


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            # authenticate user

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/home')
            else:
                messages.info(request, 'Username or Password is incorrect')

        context = {}
        return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


# @login_required(login_url='login')
def registerpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:

        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(
                    request, 'Account Created successfully for ' + user)
                return redirect('login')
        context = {'form': form}
        return render(request, 'register.html', context)

# ##############################
