from django.shortcuts import render
from .models import Quiz
from .forms import QuizForm

# Create your views here.

def create_view(request):
    context = {}

    form = QuizForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'communication\\create_view.html', context)

def list_view(request):
    context = {}
    context['dataset'] = Quiz.objects.all()

    return render(request, 'communication\\list_view.html', context)