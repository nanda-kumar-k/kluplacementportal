# Generated by Django 4.0.5 on 2022-06-25 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kluppapp', '0002_student_student_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_username',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
