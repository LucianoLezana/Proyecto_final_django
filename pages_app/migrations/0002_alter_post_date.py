# Generated by Django 4.1.1 on 2022-09-15 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
