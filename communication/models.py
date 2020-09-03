from django.db import models
from account.models import Student, Teacher
# Create your models here.


class Quiz(models.Model):
    teacher = models.ForeignKey(
        Teacher, default='Teacher', on_delete=models.SET_DEFAULT, verbose_name='Set By')
    name = models.CharField(max_length=255)
    course = models.ForeignKey(
        Course, default='Course', on_delete=models.SET_DEFAULT, verbose_name='Course Name')
    question = models.OneToManyField(Question)

    def __str__(self):
        return self.name + " ( " + self.course + " )"


class Course(models.Model):
    course_name = models.CharField(max_length=255, verbose_name='Course')
    teacher = models.ForeignKey(Teacher, default='Default Tecaher',
                                on_delete=models.SET_DEFAULT, verbose_name='Taught By')
    student = models.ForeignKey(Student, default='Default Student',
                                on_delete=models.SET_DEFAULT, verbose_name='Students Enrolled')

    def __str__(self):
        return self.course_name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, default='Default Quiz',
                             on_delete=models.SET_DEFAULT, verbose_name='From Quiz')
    question_text = models.CharField(max_length=255, verbose_name='Question')
    option1 = models.CharField(max_length=255, verbose_name='option1')
    option2 = models.CharField(max_length=255, verbose_name='option2')
    option3 = models.CharField(max_length=255, verbose_name='option3')
    option4 = models.CharField(max_length=255, verbose_name='option4')
    correctAnswer = models.CharField(
        max_length=255, verbose_name='Correct Answer')

    def __str__(self):
        return self.question_text

    def get_options(self):
        options = [self.option1, self.option2, self.option3, self.option4]
        return options

    def get_correct_answer(self):
        return self.correctAnswer


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.SET_DEFAULT, default='default question', verbose_name='Answers:')
    text = models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return self.text

    def check_answer(self):
        return self.is_correct


class StudentResponse(models.Model):
    response = models.OneToOneField(Quiz)
    student = models.ForeignKey(Student, default='Default Student',
                                on_delete=models.SET_DEFAULT, verbose_name='Response By')
    quiz = models.ForeignKey(Quiz, default='default quiz',
                             on_delete=models.SET_DEFAULT, verbose_name='Response of quiz')
    answer = models.ForeignKey(Answer, default='default answwr',
                               on_delete=models.SET_DEFAULT, verbose_name='Student Response')
