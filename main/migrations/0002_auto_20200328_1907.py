# Generated by Django 3.0.2 on 2020-03-28 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elementarymath',
            name='first',
        ),
        migrations.RemoveField(
            model_name='elementarymath',
            name='operator',
        ),
        migrations.RemoveField(
            model_name='elementarymath',
            name='second',
        ),
        migrations.AlterField(
            model_name='elementarymath',
            name='result',
            field=models.CharField(max_length=50),
        ),
    ]
