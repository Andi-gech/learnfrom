# Generated by Django 4.1.1 on 2022-09-26 22:45

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0023_answers_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='answers',
            name='image_a',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='question',
            name='image_q',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
