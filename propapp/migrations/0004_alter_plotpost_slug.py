# Generated by Django 4.1.5 on 2023-02-18 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("propapp", "0003_plotpost_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plotpost",
            name="slug",
            field=models.SlugField(unique=True),
        ),
    ]
