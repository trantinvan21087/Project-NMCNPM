# Generated by Django 4.0.4 on 2022-05-25 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_subject_alter_classes_name_alter_student_birthday_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='classes',
            field=models.ManyToManyField(to='Student.classes'),
        ),
    ]
