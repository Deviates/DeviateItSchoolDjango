# Generated by Django 4.2 on 2023-05-29 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0010_slide'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя пользователя')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта')),
                ('message', models.TextField(max_length=255, verbose_name='Введите ваше сообщение')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
