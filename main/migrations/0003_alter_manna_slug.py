# Generated by Django 3.2.7 on 2022-05-04 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220504_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manna',
            name='slug',
            field=models.SlugField(blank=True, default=' ', max_length=200),
        ),
    ]