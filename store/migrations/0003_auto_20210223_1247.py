# Generated by Django 2.2.19 on 2021-02-23 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=3000, null=True),
        ),
    ]