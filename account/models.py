from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models
from django.forms import ModelForm

# Create your models here.
class MyAccountManager(BaseUserManager):
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

        return user



class User(AbstractBaseUser):
    email = models.EmailField(verbose_name = 'email', max_length = 60, unique = True)
    username = models.CharField(max_length = 255, blank=True, null=True)
    f_name = models.CharField(max_length = 20)
    m_name = models.CharField(max_length = 20)
    l_name = models.CharField(max_length = 20)
    dob = models.DateField(null=True, blank=True)
    """
    profile_image = models.ImageField(
        default="profile_images/default.png",
        upload_to="profile_images",
        blank=True,
        null=True,
    )
    """
    date_joined = models.DateField(verbose_name = 'date joined', auto_now_add = True)
    last_login = models.DateField(verbose_name='last login', auto_now = True)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_student = models.BooleanField(default =False)
    is_teacher = models.BooleanField(default = False)
    role = ""


    def __str__(self):
        return self.f_name + " " + self.m_name+" "+ self.l_name

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['f_name', 'm_name', 'l_name', 'dob']
    objects = MyAccountManager()

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

    def is_student(self):
        return self.role == "STUDENT"

    def is_teacher(self):
        return self.role == "TEACHER"


class Student(User):
    sap_regex = RegexValidator(
        regex=r"^\+?6?\d{10,12}$", message="SAP ID must be valid"
    )
    sap_id = models.CharField(
        #validators = [sap_regex],
        max_length = 12,
        blank = False,
        null = True,
        default = None,
        unique = True
    )
    role = 'STUDENT'
    is_student = True
    department = models.CharField(max_length=10, blank=False)
    year = models.CharField(max_length=4, blank=False)
    Stud_req = ['department', 'sap_id', 'year']
    REQUIRED_FIELDS = ['username', 'department', 'year', 'sap_id']

    def __str__(self):
        return self.email

class Teacher(User):
    sap_regex = RegexValidator(
        regex=r"^\+?6?\d{10,12}$", message="SAP ID must be valid")

    teacher_sap_id = models.CharField(
        validators = [sap_regex],
        max_length=12,
        blank=False,
        null=True,
        default=None,
        unique=True
    )
    role = 'TEACHER'
    is_teacher = True
    subject = models.CharField(max_length=10, blank=False)
    teachingExperience = models.CharField(max_length=4, blank=False)
    teacher_req = ['department', 'year', 'teacher_sap_id']
    REQUIRED_FIELDS = ['username', 'subject', 'teachingExperience', 'teacher_sap_id']

    def __str__(self):
        return self.email + '( ' + self.subject + ' )'

class StudentDetail(models.Model):

    sap_id = models.CharField(verbose_name='sap id',max_length=11)
    f_name = models.CharField(verbose_name='first name', max_length=255)
    l_name = models.CharField(verbose_name='last name', max_length=255)
    email = models.EmailField(max_length = 100, verbose_name='email')
    is_student = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['f_name', 'l_name', 'is_student']

    def __str__(self):
        return self.email