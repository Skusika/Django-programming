# Generated by Django 4.2 on 2023-10-06 06:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_alter_feedback_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]