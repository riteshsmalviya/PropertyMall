# Generated by Django 4.1.5 on 2023-02-18 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("propapp", "0002_plotpost_image1_plotpost_image2_plotpost_image3_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="plotpost",
            name="slug",
            field=models.SlugField(default=50, unique=True),
        ),
    ]
