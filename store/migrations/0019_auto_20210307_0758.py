# Generated by Django 2.2.19 on 2021-03-07 06:58

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_auto_20210307_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='__str__'),
        ),
    ]