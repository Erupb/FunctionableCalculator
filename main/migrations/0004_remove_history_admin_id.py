# Generated by Django 3.0.1 on 2020-04-24 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200404_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='admin_id',
        ),
    ]
