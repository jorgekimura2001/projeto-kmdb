# Generated by Django 4.1 on 2022-12-20 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("genres", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="genre",
            options={"ordering": ("name",)},
        ),
    ]
