from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render,redirect,HttpResponse, HttpResponseRedirect
from .forms import QuizForm,QuestionForm
from .models import Question,Quiz,Result,Answer
from account.models import Teacher,Student

# Create your views here.
@login_required
def index(request):
    if request.user.is_teacher:
        quizzes = Quiz.objects.filter(teacher=request.user)
    else:
        quizzes = Quiz.objects.all()
    context = {'quizzes':quizzes}
    return render(request, 'index.html', context)


@login_required
def create_quiz(request):
    if request.user.is_student:
        return HttpResponseRedirect('index')
    else:
        form = QuizForm()
        context = {
            'form':form
        }
        return render(request, 'create_quiz.html', context)
@login_required
def add_questions(request):
    if request.method == 'POST':
        quiz_id = request.POST['object']
        instance = Quiz.objects.get(id=quiz_id)
        form = QuestionForm(request.POST)
        if form.is_valid():
            u = form.save(commit=False)
            u.quiz = instance
            u.save()

        score = Question.objects.filter(quiz=instance).aggregate(Count('question_text'))['question_text__count']+1
        #context = {}
        if score < instance.total_questions:
            context = {'quiz': quiz_id,'form': QuestionForm,}
        elif(score == instance.total_questions):
            context = {'last': True,'quiz': quiz_id,'form': QuestionForm}
        else:
            return redirect('index')
        return render(request, 'add_questions.html', context)

    else:
        try:
            subject = request.GET['subject']
            total_questions = request.GET['total_questions']
            teacher = Teacher.objects.get(email=request.user)
            quiz = Quiz.objects.create(subject=subject, total_questions=total_questions, teacher=teacher)
            form = QuestionForm
            if total_questions == '1': #Only 1 Question
                last = True
            else:
                last = False
                context = {
                'last':last,
                'form':form,
                'quiz':quiz.id
                }
            return render(request, 'add_questions.html', context)
        except:
            return render(request,'questions')


@login_required
def delete(request, quiz_id):
    if request.user.is_student:
        return HttpResponse('UNAUTHORIZED ACCESS')
        #return HttpResponseRedirect('index')

    else:
        Quiz.objects.filter(id=quiz_id).delete()
        return redirect('index')


@login_required
def display(request, quiz_id):
    questions = Question.objects.filter(quiz=quiz_id)
    quiz = Quiz.objects.get(id=quiz_id)
    if request.method == 'POST':
        student = Student.objects.get(email=request.user)
        score = 0
        for question in questions:
            answer = request.POST['option_'+str(question.id)]
            Answer.objects.create(student=student, question=question, answer=answer)
            if answer == question.correct_answer:
                score = score + 1
        result = Result.objects.create(student=student, quiz=quiz, score_obtained=score)
        answers = Answer.objects.filter(student=student, question__in=questions)
        context = {
            'answers': answers,
            'result' : result
        }
        return render(request, 'result.html', context)
    elif request.user.is_student:
        student = Student.objects.get(email=request.user)
        if Result.objects.filter(quiz=quiz, student=student).exists():
            is_attempted = True
        else:
            is_attempted = False
        context = {
            'attempted': is_attempted,
            'questions':questions,
            'quiz':quiz_id
        }
    else:
        context = {
            'questions':questions,
            'quiz': quiz_id
        }
    return render(request, 'display.html', context)


@login_required
def update(request, question_id):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        question = Question.objects.get(id=question_id)
        if form.is_valid():
            question.question_text = form.cleaned_data['question_text']
            question.option1 = form.cleaned_data['option1']

            question.option2 = form.cleaned_data['option2']

            question.option3 = form.cleaned_data['option3']

            question.option4 = form.cleaned_data['option4']
            question.correct_answer = form.cleaned_data['correct_answer']
            question.save()
        return redirect('display', question.quiz.id)

    else:
        if request.user.is_student:
            return HttpResponse('UNAUTHORIZED ACCESS')
        else:
            question = Question.objects.get(id=question_id)
            form = QuestionForm(instance=question)
            context = {
                'form': form,
                'question':question
            }
            return render(request, 'update.html', context)

@login_required
def result(request, quiz_id, student_id=None):
    questions = Question.objects.filter(quiz=quiz_id)
    if request.user.is_student:
        student = Student.objects.get(email=request.user)
    else:
        student = Student.objects.get(sap_id=student_id)
    answers = Answer.objects.filter(student=student, quiz=quiz_id)
    context = {
        'answers': answers,
        'result': result
    }
    return render(request, 'result.html', context)

@login_required
def result_list(request, quiz_id):
    if request.user.is_student:
        return HttpResponse('You are not authorized to view this page')
    else:
        results = Result.objects.filter(quiz=quiz_id)
        context = {
            'results' : results,
            'quiz' : quiz_id
        }
        return render(request,'result_list.html',context)
