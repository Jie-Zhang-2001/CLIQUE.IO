# Generated by Django 3.0.6 on 2020-06-20 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_auto_20200620_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmodel',
            name='owner',
            field=models.IntegerField(default=-1),
        ),
    ]
