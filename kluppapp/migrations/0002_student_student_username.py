# Generated by Django 4.0.5 on 2022-06-25 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kluppapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_username',
            field=models.CharField(default=None, max_length=200, unique=True),
        ),
    ]