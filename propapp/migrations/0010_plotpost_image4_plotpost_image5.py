# Generated by Django 4.1.5 on 2023-02-21 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("propapp", "0009_alter_plotpost_admap"),
    ]

    operations = [
        migrations.AddField(
            model_name="plotpost",
            name="image4",
            field=models.ImageField(blank=True, null=True, upload_to="propapp\\images"),
        ),
        migrations.AddField(
            model_name="plotpost",
            name="image5",
            field=models.ImageField(blank=True, null=True, upload_to="propapp\\images"),
        ),
    ]