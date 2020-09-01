from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.db import models
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import StudentSignUpForm, TeacherSignUpForm

from django.template import loader
from django.http import HttpResponse
from django.forms import modelform_factory



class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    return render(request, 'home.html')

@login_required
def index(request):
    return render(request,'index.html')



def studentSignup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = StudentSignUpForm()
    return render(request, 'signup.html', {'form': form})

def TeacherSignup(request):
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = TeacherSignUpForm()
    return render(request, 'teacherSignup.html', {'form': form})

def logout(request):
    return (HttpResponse('LOGGED OUT'))

