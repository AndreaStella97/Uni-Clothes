# Generated by Django 2.2.19 on 2021-02-23 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210223_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinstock',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('t-shirt', 'T-Shirt'), ('shirt', 'Shirt'), ('sweater', 'Sweater'), ('jeans', 'Jeans'), ('pants', 'Pants'), ('skirt', 'Skirt'), ('jacket', 'Jacket'), ('shoes', 'Shoes'), ('socks', 'Socks')], max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('unisex', 'Unisex')], max_length=10),
        ),
        migrations.AlterField(
            model_name='productinstock',
            name='size',
            field=models.CharField(choices=[('xxs', 'XXS'), ('xs', 'XS'), ('s', 'S'), ('m', 'M'), ('l', 'L'), ('xl', 'XL'), ('xxl', 'XXL')], max_length=5),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='color',
            field=models.CharField(choices=[('blue', 'Blue'), ('red', 'Red'), ('green', 'Green'), ('yellow', 'Yellow'), ('brown', 'Brown'), ('orange', 'Orange'), ('pink', 'Pink'), ('black', 'Black'), ('white', 'White'), ('grey', 'Grey'), ('purple', 'Purple')], max_length=10),
        ),
    ]
