from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from communication import models
from django.urls import reverse_lazy

# Create your views here.

class IndexView(TemplateView):
    template_name='index.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['injectme']='hello'
        return context


class ChapterListView(ListView):
    model=models.McqExam


class QuestionDetailView(DetailView):
    context_object_name='question'
    model=models.McqExam
    template_name='communication/quiz_detail.html'

class ChapterCreateView(CreateView):
    fields=('exam_topic',)
    model=models.McqExam

class QuestionUpdateView(UpdateView):
    fields=('id','question','option_1','option_2','option_3','option_4','correct_ans')
    model=models.Question

class ChapterDeleteView(DeleteView):
    model=models.McqExam
    success_url=reverse_lazy('quiz:list')

def student_chp_lst(request):
    topic=models.McqExam.objects.all()
    return render(request,'communication/student_chp_lst.html',{'topic':topic})

def question_detail(request,chp_pk):

    if request.method=='POST':

        answer=request.POST.get('ans')
        question=request.POST.get('luck')

        question=models.Question.objects.get(id=question)
        student_response=models.Student_Response(student_response=answer,question=question)

        student_response.save()
        return redirect('communication:detail_fun',chp_pk)

    else:
        questions=models.Question.objects.filter(mcq_exam=chp_pk)

        return render(request,'communication/detail.html',{'questions':questions})
