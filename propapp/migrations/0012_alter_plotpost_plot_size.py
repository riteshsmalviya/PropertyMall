# Generated by Django 4.1.5 on 2023-02-21 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("propapp", "0011_plotpost_plot_size"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plotpost",
            name="plot_size",
            field=models.CharField(max_length=225),
        ),
    ]
