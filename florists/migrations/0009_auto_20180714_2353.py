# Generated by Django 2.0.1 on 2018-07-14 15:53

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('florists', '0008_client_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='questions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=[], size=None),
        ),
    ]