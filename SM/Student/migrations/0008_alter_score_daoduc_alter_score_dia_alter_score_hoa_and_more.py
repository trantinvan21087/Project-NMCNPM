# Generated by Django 4.0.4 on 2022-05-26 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0007_alter_score_unique_together_score_daoduc_score_dia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='Daoduc',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='score',
            name='Dia',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='score',
            name='Hoa',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='score',
            name='Ly',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='score',
            name='Sinh',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='score',
            name='Su',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='score',
            name='TheDuc',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='score',
            name='Toan',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='score',
            name='Van',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
