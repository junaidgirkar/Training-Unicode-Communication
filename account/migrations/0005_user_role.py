# Generated by Django 3.0.4 on 2020-09-10 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200910_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='DefaultRole', max_length=100),
        ),
    ]
