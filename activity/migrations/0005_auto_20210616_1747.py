# Generated by Django 3.2.4 on 2021-06-16 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_alter_git_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='git_user',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='git_user',
            name='email',
            field=models.EmailField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='git_user',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
