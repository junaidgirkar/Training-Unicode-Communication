from account.models import *
from django.db import models
from django.urls import reverse

# Create your models here.
class McqExam(models.Model):
	exam_topic=models.CharField(max_length=20)
	#teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
	def __str__(self):
		return self.exam_topic

	def get_absolute_url(self):
		return reverse("list",kwargs={'pk':self.pk})

class Question(models.Model):
	mcq_exam=models.ForeignKey(McqExam,on_delete=models.CASCADE,related_name='mcq_exam')
	question=models.CharField(max_length=300)
	option_1=models.CharField(max_length=300)
	option_2=models.CharField(max_length=300)
	option_3=models.CharField(max_length=300)
	option_4=models.CharField(max_length=300)
	correct_ans=models.CharField(max_length=1)

	def __str__(self):
		return self.question

	def get_absolute_url(self):
		return reverse("quiz:detail",kwargs={'pk':self.pk})




class Student_Response(models.Model):
	question=models.ForeignKey(Question,on_delete=models.CASCADE)
	student=models.ForeignKey(Student,on_delete=models.CASCADE)
	student_response=models.CharField(max_length=1)

	#return self.question, self.correctAnswer


	def __str__(self):
		return 'response'