# Generated by Django 4.1 on 2022-09-13 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0002_subject_is_requestable_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='year',
        ),
    ]
