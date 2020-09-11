from django.shortcuts import render

# Create your views here.
from django.db.models import Count
from django.shortcuts import render,redirect
from .forms import QuizForm,QuestionForm
from .models import Question,Quiz,Result,Answer
from account.models import Teacher,Student


# Create your views here.

def index(request):
    if request.user.is_teacher:
        quizzes = Quiz.objects.filter(teacher=request.user)
    else:
        quizzes = Quiz.objects.all()
    context = {
        'quizzes' : quizzes
    }
    return render(request,'index.html',context)

def create_info(request):
    form = QuizForm()
    context = {
        'form' : form
    }
    return render(request,'create_info.html',context)


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
        if count > instance.total_marks:
            return redirect('index')
        elif count < instance.total_marks:
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
        return render(request,'create.html',context)

    else:
        topic = request.GET['topic']
        total_marks = request.GET['total_marks']
        teacher = Teacher.objects.get(email=request.user)
        quiz = Quiz.objects.create(topic=topic,total_marks=total_marks,teacher=teacher)
        form = QuestionForm()
        context = {
            'form' : form,
            'quiz' : quiz.id
        }
        return render(request,'create.html',context)

def delete(request,quiz_id):
    Quiz.objects.filter(id=quiz_id).delete()
    return redirect('index')


def display(request,quiz_id):
    questions = Question.objects.filter(quiz=quiz_id)
    quiz = Quiz.objects.get(id=quiz_id)
    if request.method == 'POST':
        student = Student.objects.get(email=request.user)
        marks = 0
        for question in questions:
            answer = request.POST['choice' + '_' + str(question.id)]
            Answer.objects.create(student=student,question=question,answer=answer)
            if answer == question.correct_choice:
                marks = marks + 1
        Result.objects.create(student=student,quiz=quiz,marks_obtained=marks)
        return redirect('index')

    else:
        student = Student.objects.filter(email=request.user)
        if Result.objects.filter(quiz=quiz,student__in=student).exists():
            attempted = True
        else:
            attempted = False
        context = {
            'attempted' : attempted,
            'questions' : questions,
            'quiz' : quiz_id
        }
        return render(request,'display.html',context)

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
        return redirect('index')

    else:
        question = Question.objects.get(id=question_id)
        form = QuestionForm(instance=question)
        context = {
            'form' : form,
            'question' : question
        }
        return render(request,'update.html',context)