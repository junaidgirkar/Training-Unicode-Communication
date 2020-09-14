from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .managers import *
import re
import json

from django.db import models
from django.core.exceptions import ValidationError, ImproperlyConfigured
from django.core.validators import MaxValueValidator, validate_comma_separated_integer_list
from django.utils.timezone import now
from django.conf import settings
from django.utils.translation import ugettext as _
from model_utils.managers import InheritanceManager
from django.db.models.signals import pre_save, post_save
import io

from django.contrib.auth.models import User
from django.contrib import messages
from django.forms import ModelForm
from django.utils.html import escape, mark_safe

# Create your models here.
"""class MyAccountManager(BaseUserManager):
    def create_user(self, f_name, m_name, l_name, dob, email, password=None,):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError("User must enter a password")

        user = self.model(
            email = self.normalize_email(email),
            f_name = f_name,
            m_name = m_name,
            l_name=l_name,
            dob = dob,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,f_name,m_name,l_name,dob, email, password):
        user = self.create_user(email = self.normalize_email(email),
                                f_name=f_name,
                                m_name=m_name,
                                l_name=l_name,
                                dob=dob,
                                password= password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user"""


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dob = models.DateField(null=True, blank=True)

    date_joined = models.DateField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    role = models.CharField(max_length=100, default='DefaultRole')

    def __str__(self):
        return self.first_name + " " + self.middle_name+" " + self.last_name

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'middle_name', 'last_name', 'dob']
    objects = UserManager()

    def save(self, *args, **kwargs):
        self.username = self.email
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True


class Teacher(User):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, parent_link=True)
    user.is_teacher = True
    sap_regex = RegexValidator(
        regex=r"^\+?6?\d{10,12}$", message="SAP ID must be valid")

    teacher_sap_id = models.CharField(
        validators=[sap_regex],
        max_length=12,
        blank=False,
        null=True,
        default=None,
        unique=True,

    )

    #type = models.CharField(max_length=100)
    subject = models.CharField(max_length=15, blank=False)
    teachingExperience = models.CharField(max_length=4, blank=False)
    objects = TeacherManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email + '( ' + self.subject + ' )'


class Student(User):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, parent_link=True)
    user.is_student = True
    User.is_student = True
    is_student = True
    sap_id = models.CharField(
        #validators = [sap_regex],
        max_length=12,
        blank=False,
        null=True,
        default=None,
        unique=True
    )

    type = models.CharField(max_length=100)
    department = models.CharField(max_length=10, blank=False)
    year = models.CharField(max_length=4, blank=False)
    objects = StudentManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.user.email


"""
class Quiz(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    topic = models.CharField(max_length=30, default='Topic')
    total_marks = models.IntegerField(default=0)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name_plural = 'Quizzes'


class McqExam(models.Model):
	exam_topic=models.CharField(max_length=20)
	teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
	def __str__(self):
		return self.exam_topic

class Question(models.Model):
	mcq_exam=models.ForeignKey(McqExam,on_delete=models.CASCADE, default='DefaultMCQExam')
	question=models.CharField(max_length=300, default='DefaultQuestion')
	option_1=models.CharField(max_length=300, default='DefOpt1')
	option_2=models.CharField(max_length=300, default='DefOpt2')
	option_3=models.CharField(max_length=300, default='DefOpt3')
	option_4=models.CharField(max_length=300, default='DefOpt4')
	correct_ans=models.CharField(max_length=100, default='CorrectAnswer')

	def __str__(self):
		return self.mcq_exam.exam_topic



class Student_Response:
	question=models.ForeignKey(Question,on_delete=models.CASCADE)
	student=models.ForeignKey(Student,on_delete=models.CASCADE)
	student_response=models.CharField(max_length=1)

	def __str__(self):
		return 'response'
		"""
