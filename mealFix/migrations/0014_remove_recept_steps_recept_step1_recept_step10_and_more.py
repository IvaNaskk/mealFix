# Generated by Django 4.1 on 2022-08-31 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealFix', '0013_rename_rating_recept_servings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recept',
            name='steps',
        ),
        migrations.AddField(
            model_name='recept',
            name='step1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recept',
            name='step10',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recept',
            name='step2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recept',
            name='step3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recept',
            name='step4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recept',
            name='step5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recept',
            name='step6',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recept',
            name='step7',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recept',
            name='step8',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recept',
            name='step9',
            field=models.TextField(blank=True, null=True),
        ),
    ]
