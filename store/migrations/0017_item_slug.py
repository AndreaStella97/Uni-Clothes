# Generated by Django 2.2.19 on 2021-03-07 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20210307_0622'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='prova'),
        ),
    ]
