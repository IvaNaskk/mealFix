# Generated by Django 4.1 on 2022-08-30 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealFix', '0010_course_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='recept',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]