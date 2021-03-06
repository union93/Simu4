# Generated by Django 3.1 on 2020-08-28 22:49

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200829_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True, validators=[accounts.models.validate_email], verbose_name='email'),
        ),
    ]
