from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.db import models
from .models import StudentDetail
from django.template import loader
from django.http import HttpResponse
from django.forms import modelform_factory
from .forms import StudentDetailForm

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('teachers:quiz_change_list')
        else:
            return redirect('students:quiz_list')
    return render(request, 'account/home.html')

def studentDetail(request):
    if request.method=='POST':
        form = StudentDetailForm(request.POST)
        if form.is_valid():
            u = form.save()
            users = StudentDetail.objects.all()

            return render(request, 'account\\display.html', {'users':users})

    else:
        form_class = StudentDetailForm
    return render(request, 'account\\studentDetail.html', {'form':form_class})

