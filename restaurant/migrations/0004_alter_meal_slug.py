# Generated by Django 4.2.6 on 2023-10-31 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_meal_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
