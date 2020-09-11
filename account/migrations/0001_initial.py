# Generated by Django 3.1 on 2020-09-11 19:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('f_name', models.CharField(max_length=20)),
                ('m_name', models.CharField(max_length=20)),
                ('l_name', models.CharField(max_length=20)),
                ('dob', models.DateField(blank=True, null=True)),
                ('date_joined', models.DateField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('role', models.CharField(default='DefaultRole', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='McqExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_topic', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='account.user')),
                ('sap_id', models.CharField(default=None, max_length=12, null=True, unique=True)),
                ('type', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=4)),
            ],
            options={
                'abstract': False,
            },
            bases=('account.user',),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='account.user')),
                ('teacher_sap_id', models.CharField(default=None, max_length=12, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='SAP ID must be valid', regex='^\\+?6?\\d{10,12}$')])),
                ('subject', models.CharField(max_length=15)),
                ('teachingExperience', models.CharField(max_length=4)),
            ],
            options={
                'abstract': False,
            },
            bases=('account.user',),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(default='DefaultQuestion', max_length=300)),
                ('option_1', models.CharField(default='DefOpt1', max_length=300)),
                ('option_2', models.CharField(default='DefOpt2', max_length=300)),
                ('option_3', models.CharField(default='DefOpt3', max_length=300)),
                ('option_4', models.CharField(default='DefOpt4', max_length=300)),
                ('correct_ans', models.CharField(default='CorrectAnswer', max_length=100)),
                ('mcq_exam', models.ForeignKey(default='DefaultMCQExam', on_delete=django.db.models.deletion.CASCADE, to='account.mcqexam')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(default='Topic', max_length=30)),
                ('total_marks', models.IntegerField(default=0)),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.teacher')),
            ],
            options={
                'verbose_name_plural': 'Quizzes',
            },
        ),
        migrations.AddField(
            model_name='mcqexam',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.teacher'),
        ),
    ]
