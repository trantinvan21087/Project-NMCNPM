# Generated by Django 4.0.4 on 2022-05-26 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0006_student_house_location_alter_student_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='score',
            unique_together={('semester', 'students')},
        ),
        migrations.AddField(
            model_name='score',
            name='Daoduc',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='Dia',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='Hoa',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='Ly',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='Sinh',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='Su',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='TheDuc',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='Toan',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='Van',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.CharField(choices=[('Toán', 'Toán'), ('Lý', 'Lý'), ('Hóa', 'Hóa'), ('Sinh', 'Sinh'), ('Sử', 'Sử'), ('Địa', 'Địa'), ('Văn', 'Văn'), ('Đạo đức', 'Đạo đức'), ('Thể dục', 'Thể dục')], max_length=200, null=True, unique=True),
        ),
        migrations.RemoveField(
            model_name='score',
            name='score',
        ),
        migrations.RemoveField(
            model_name='score',
            name='subject',
        ),
    ]