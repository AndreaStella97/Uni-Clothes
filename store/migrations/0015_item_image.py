# Generated by Django 2.2.19 on 2021-03-07 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20210307_0406'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]