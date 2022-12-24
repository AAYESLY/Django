# Generated by Django 4.1 on 2022-12-13 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("firstapp", "0003_user_userage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("age", models.IntegerField(default=0)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="Test",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "contact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="firstapp.contact",
                    ),
                ),
            ],
        ),
    ]