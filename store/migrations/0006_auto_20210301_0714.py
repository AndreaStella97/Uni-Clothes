# Generated by Django 2.2.19 on 2021-03-01 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20210223_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('t-shirt', 'T-Shirt'), ('shirt', 'Shirt'), ('sweater', 'Sweater'), ('jeans', 'Jeans'), ('pants', 'Pants'), ('jacket', 'Jacket'), ('shoes', 'Shoes'), ('socks', 'Socks')], max_length=20),
        ),
    ]