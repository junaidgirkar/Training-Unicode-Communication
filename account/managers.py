from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):

    use_in_migrations = True


    def create_user(self, email, first_name,is_teacher,is_student, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        #if not username:
         #   raise ValueError('Users must have a username')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            is_student=is_student,
            is_teacher=is_teacher,
            email=self.normalize_email(email),
            #user.set_password(self.cleaned_data["password"])
            #username=username
        )

        user.set_password(password)
        #user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email,first_name, last_name, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            password=password,
            #username=username
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        is_student = is_student,
        is_teacher = is_teacher,
        user.save(using=self._db)
        return user


class StudentManager(BaseUserManager):
    use_in_migrations = True


    def create_user(self, email, first_name,is_student, is_teacher, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        #if not username:
         #   raise ValueError('Users must have a username')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            is_student=is_student,
            is_teacher=is_teacher,
            email=self.normalize_email(email),
            #user.set_password(self.cleaned_data["password"])
            #username=username
        )

        user.set_password(password)
        #user.set_password(password)
        user.save(using=self._db)
        return user


class TeacherManager(BaseUserManager):
    use_in_migrations = True


    def create_user(self, email, first_name,is_student,is_teacher, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        #if not username:
         #   raise ValueError('Users must have a username')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            is_student=is_student,
            is_teacher=is_teacher,
            #user.set_password(self.cleaned_data["password"])
            #username=username
        )

        user.set_password(self.cleaned_data["password"])
        #user.set_password(password)
        user.save(using=self._db)
        return user
