# Generated by Django 4.1.1 on 2022-09-23 17:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0016_remove_like_date_remove_like_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='likes',
            field=models.ManyToManyField(related_name='answers_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='like',
        ),
    ]
