# Generated by Django 2.0.1 on 2018-06-15 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('florists', '0003_client_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='con_email',
            field=models.CharField(max_length=300, verbose_name='Contact No.'),
        ),
    ]
