# Generated by Django 4.1.4 on 2022-12-15 11:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("forum", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="messages",
            options={"verbose_name_plural": "messages"},
        ),
        migrations.AddField(
            model_name="forum",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="forum",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]