# Generated by Django 3.1 on 2020-08-31 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='User', max_length=10),
            preserve_default=False,
        ),
    ]
