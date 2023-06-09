# Generated by Django 4.2 on 2023-04-12 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0006_alter_aboutnumber_alumni_alter_aboutnumber_company_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='team_image/', verbose_name='Фотография')),
                ('name', models.CharField(max_length=244, verbose_name='ФИО')),
                ('work', models.CharField(max_length=255, verbose_name='Работа')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('github', models.URLField(blank=True, null=True, verbose_name='GitHub')),
                ('whatsapp', models.URLField(blank=True, null=True, verbose_name='Whatsapp')),
            ],
            options={
                'verbose_name': 'Команда',
                'verbose_name_plural': 'Команда',
            },
        ),
    ]
