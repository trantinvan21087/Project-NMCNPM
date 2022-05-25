# Generated by Django 4.0.4 on 2022-05-25 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0003_teacher_classes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('học kỳ 1', 'học kỳ 1'), ('học kỳ 2', 'học kỳ 2')], max_length=200, null=True)),
                ('score', models.CharField(max_length=2, null=True)),
                ('Students', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Student.student')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Student.subject')),
            ],
            options={
                'unique_together': {('score', 'Students', 'subject')},
            },
        ),
    ]
