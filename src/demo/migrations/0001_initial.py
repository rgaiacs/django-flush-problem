# Generated by Django 4.2.3 on 2024-12-23 12:07

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bar",
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
            ],
        ),
        migrations.CreateModel(
            name="Foo",
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
                ("bars", models.ManyToManyField(blank=True, to="demo.bar")),
            ],
        ),
        migrations.AddField(
            model_name="bar",
            name="foos",
            field=models.ManyToManyField(blank=True, to="demo.foo"),
        ),
    ]
