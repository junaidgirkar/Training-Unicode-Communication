# Generated by Django 3.1 on 2020-09-11 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='topic',
            new_name='subject',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='total_marks',
            new_name='total_questions',
        ),
    ]
