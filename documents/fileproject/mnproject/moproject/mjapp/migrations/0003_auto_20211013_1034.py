# Generated by Django 3.2.8 on 2021-10-13 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mjapp', '0002_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='desc',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='food',
            name='nam',
            field=models.CharField(max_length=50),
        ),
    ]
