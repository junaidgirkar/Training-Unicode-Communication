# Generated by Django 3.0.4 on 2020-09-10 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_student',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='is_teacher',
            field=models.BooleanField(default=True),
        ),
    ]