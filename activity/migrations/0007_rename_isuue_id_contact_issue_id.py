# Generated by Django 3.2.4 on 2021-06-24 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0006_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='isuue_id',
            new_name='issue_id',
        ),
    ]
