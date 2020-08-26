from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
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

def detail_view(request, id):
    context = {}
    context["data"] = Quiz.objects.get(id = id)

    return render(request, 'communication\\detail_view.html', context)

def update_view(request, id):
    context = {}
    # fetch object related to passed it
    obj = get_object_or_404(Quiz, id=id)

    #pass the obj as instance in form
    form = QuizForm(request.POST or None, instance = obj)

    #Save data and redirect
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)

    #add form directry to context
    context['form'] = form

    return render(request, 'communication\\update_view.html', context)

