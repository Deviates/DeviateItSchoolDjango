# Generated by Django 4.2 on 2023-04-12 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_alter_setting_email_alter_setting_locate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='maps',
        ),
        migrations.AddField(
            model_name='setting',
            name='address_url',
            field=models.URLField(blank=True, max_length=1000, null=True, verbose_name='Ссылка на адрес'),
        ),
    ]
