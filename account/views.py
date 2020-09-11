
from .forms import *
from django.db.models import Count
from django.shortcuts import render,redirect,reverse


from django.contrib.auth.decorators import login_required, permission_required

from django.views.generic import DetailView, ListView, TemplateView


from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout



class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    return render(request, 'home.html')

@login_required
def base_index(request):
    return render(request,'index.html')



def studentSignup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            role = form.cleaned_data.get('role')
            #user = authenticate(username=username, password=raw_password)
            print(role)
            login(request, user)
            return redirect('home')
    else:
        form = StudentSignUpForm()
    return render(request, 'signup.html', {'form': form})

def TeacherSignup(request):
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            
            role = form.cleaned_data.get('role')
            #user = authenticate(username=username, password=raw_password)
            print(role)
            login(request, user)
            return redirect('home')
    else:
        form = TeacherSignUpForm()
    return render(request, 'teacherSignup.html', {'form': form})

