from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Quiz
from .forms import QuizForm
from django.views import View
# Create your views here.

class create_view(View):
    def get(self, request):
        context = {}

        form = QuizForm(request.POST or None)
        if form.is_valid():
            form.save()
        context['form'] = form
        return render(request, 'communication\\create_view.html', context)
    def post(self,request):
        context = {}

        form = QuizForm(request.POST or None)
        if form.is_valid():
            form.save()
        context['form'] = form
        return render(request, 'communication\\create_view.html', context)


class list_view(View):
    def get(self, request):
        context = {}
        context['dataset'] = Quiz.objects.all()

        return render(request, 'communication\\list_view.html', context)

class detail_view(View):
    def get(self, request, id):
        context = {}
        context["data"] = Quiz.objects.get(id = id)

        return render(request, 'communication\\detail_view.html', context)

class update_view(View):
    def get(self, request, id):
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

    def post(self, request, id):
        context = {}
        # fetch object related to passed it
        obj = get_object_or_404(Quiz, id=id)
        # pass the obj as instance in form
        form = QuizForm(request.POST or None, instance=obj)
        # Save data and redirect
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/" + id)
        # add form directry to context
        context['form'] = form
        return render(request, 'communication\\update_view.html', context)

class delete_view(View):
    def get(self, request, id):
        context = {}
        #fetch the obj related to passed id
        obj = get_object_or_404(Quiz, id = id)

        if request.method == 'POST':
            # Delete Object
            obj.delete()
            # After Deleting Redirect to Home Page
            return HttpResponseRedirect('/')
        return render(request, "communication\\delete_view.html", context)

    def post(self, request, id):
        context = {}
        # fetch the obj related to passed id
        obj = get_object_or_404(Quiz, id=id)

        if request.method == 'POST':
            # Delete Object
            obj.delete()
            # After Deleting Redirect to Home Page
            return HttpResponseRedirect('/')
        return render(request, "communication\\delete_view.html", context)


def result_view(request):
    score = 0
    args = {score: score}
    return render(request, 'communication\\result_view.html', args)