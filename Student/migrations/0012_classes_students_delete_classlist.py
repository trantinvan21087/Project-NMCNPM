# Generated by Django 4.0.4 on 2022-06-07 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0011_teacher_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='Students',
            field=models.ManyToManyField(to='Student.student'),
        ),
        migrations.DeleteModel(
            name='ClassList',
        ),
    ]
