# Generated by Django 4.2 on 2023-04-12 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_aboutnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutnumber',
            name='alumni',
            field=models.CharField(max_length=255, verbose_name='Количество выпускников'),
        ),
        migrations.AlterField(
            model_name='aboutnumber',
            name='company',
            field=models.CharField(max_length=255, verbose_name='Количество комании в которых работают'),
        ),
        migrations.AlterField(
            model_name='aboutnumber',
            name='students',
            field=models.CharField(max_length=255, verbose_name='Количество студентов'),
        ),
    ]
