# Generated by Django 4.1 on 2022-12-12 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("firstapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="password",),
    ]
