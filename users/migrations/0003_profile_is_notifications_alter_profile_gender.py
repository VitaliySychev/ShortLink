# Generated by Django 5.0 on 2023-12-15 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_options_profile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_notifications',
            field=models.BooleanField(default=False, verbose_name='Соглашение на отправку уведомлений на почту'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('male', 'Мужской'), ('female', 'Женский')], default='male', max_length=6, verbose_name='Выбрать пол'),
        ),
    ]
