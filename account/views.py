
from .forms import *
from django.db.models import Count
from django.shortcuts import render,redirect,reverse


from django.contrib.auth.decorators import login_required, permission_required

from django.views.generic import DetailView, ListView, TemplateView

from .forms import QuestionForm
from .models import Quiz, Question
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



def index(request):
    quizzes = Quiz.objects.all()
    context = {
        'quizzes' : quizzes
    }
    return render(request,'quiz/index.html',context)

def create_info(request):
    form = QuizForm()
    context = {
        'form' : form
    }
    return render(request,'quiz/create_info.html',context)


def create(request):
    if request.method == 'POST':
        quiz_id = request.POST['object']
        instance = Quiz.objects.get(id=quiz_id)
        form = QuestionForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.quiz = instance
            temp.save()
        count = Question.objects.filter(quiz=instance).aggregate(Count('question_text'))['question_text__count'] + 1
        if count != instance.total_marks :
            context = {
                'quiz' : quiz_id,
                'form' : QuestionForm()
            }
        else:
            context = {
                'last' : True,
                'quiz' : quiz_id,
                'form' : QuestionForm
            }
        return render(request,'quiz/create.html',context)

    else:
        topic = request.GET['topic']
        total_marks = request.GET['total_marks']
        teacher = Teacher.objects.get(email=request.user.email)
        quiz = Quiz.objects.create(topic=topic,total_marks=total_marks,teacher=teacher)
        form = QuestionForm()
        context = {
            'form' : form,
            'quiz' : quiz.id
        }
        return render(request,'quiz/create.html',context)

def delete(request,quiz_id):
    Quiz.objects.filter(id=quiz_id).delete()
    return redirect(request.META['HTTP_REFERER'])


def display(request,quiz_id):
    questions = Question.objects.filter(quiz=quiz_id)
    context = {
        'questions' : questions
    }
    return render(request,'quiz/display.html',context)

def update(request,question_id):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        question = Question.objects.get(id=question_id)
        if form.is_valid():
            question.question_text = form.cleaned_data['question_text']
            question.choice1 = form.cleaned_data['choice1']
            question.choice2 = form.cleaned_data['choice2']
            question.choice3 = form.cleaned_data['choice3']
            question.choice4 = form.cleaned_data['choice4']
            question.correct_choice = form.cleaned_data['correct_choice']
            question.save()
        return redirect(reverse('index'))

    else:
        question = Question.objects.get(id=question_id)
        form = QuestionForm(instance=question)
        context = {
            'form' : form,
            'question' : question
        }
        return render(request,'quiz/update.html',context)