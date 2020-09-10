# Generated by Django 3.1 on 2020-09-10 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_merge_20200910_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizTakers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_answers', models.IntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='takenquiz',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='takenquiz',
            name='student',
        ),
        migrations.AlterModelOptions(
            name='quiz',
            options={'ordering': ['created'], 'verbose_name_plural': 'Quizzes'},
        ),
        migrations.AlterModelManagers(
            name='student',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='teacher',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='text',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='student',
            name='quizzes',
        ),
        migrations.AddField(
            model_name='question',
            name='label',
            field=models.CharField(default='Default', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='quiz',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='description',
            field=models.CharField(default='Default', max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='questions_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='quiz',
            name='roll_out',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='quiz',
            name='slug',
            field=models.SlugField(default='Default'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.quiz'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='name',
            field=models.CharField(max_length=1000),
        ),
        migrations.DeleteModel(
            name='StudentAnswer',
        ),
        migrations.DeleteModel(
            name='TakenQuiz',
        ),
        migrations.AddField(
            model_name='response',
            name='answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.answer'),
        ),
        migrations.AddField(
            model_name='response',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.question'),
        ),
        migrations.AddField(
            model_name='response',
            name='quiztaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.quiztakers'),
        ),
        migrations.AddField(
            model_name='quiztakers',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.quiz'),
        ),
        migrations.AddField(
            model_name='quiztakers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]