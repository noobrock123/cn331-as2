# Generated by Django 4.1 on 2022-09-13 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0005_remove_year_subjects_year_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year',
            name='subjects',
            field=models.ManyToManyField(blank=True, related_name='subjects', to='user_page.subject'),
        ),
    ]
