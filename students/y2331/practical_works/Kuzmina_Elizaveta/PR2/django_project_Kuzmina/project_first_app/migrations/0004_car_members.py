# Generated by Django 3.0.5 on 2020-04-03 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0003_auto_20200402_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='members',
            field=models.ManyToManyField(through='project_first_app.Ownership', to='project_first_app.CarOwner'),
        ),
    ]