# Generated by Django 4.1.1 on 2022-09-19 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_like_value_alter_like_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='cat_name',
            field=models.CharField(choices=[('science', 'science'), ('code', 'code'), ('math', 'math'), ('other', 'other')], default='math', max_length=20),
        ),
        migrations.DeleteModel(
            name='Catagory',
        ),
    ]
