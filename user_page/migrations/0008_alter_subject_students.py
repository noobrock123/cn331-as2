# Generated by Django 4.1 on 2022-09-14 07:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_page', '0007_subject_year_delete_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='subjects', to=settings.AUTH_USER_MODEL),
        ),
    ]
