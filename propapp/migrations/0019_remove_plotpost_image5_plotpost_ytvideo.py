# Generated by Django 4.1.5 on 2023-03-21 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("propapp", "0018_alter_plotpost_search_result"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="plotpost",
            name="image5",
        ),
        migrations.AddField(
            model_name="plotpost",
            name="ytvideo",
            field=models.TextField(default="hello"),
        ),
    ]
