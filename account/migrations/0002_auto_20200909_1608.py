# Generated by Django 3.1 on 2020-09-09 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='check_student',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='check_teacher',
            field=models.BooleanField(default=False),
        ),
    ]
