# Generated by Django 4.0.2 on 2022-06-26 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kluppapp', '0003_alter_student_student_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultycourses',
            name='f_section',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='studentcourses',
            name='s_section',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
