# Generated by Django 3.1.5 on 2021-02-12 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ECOM', '0013_auto_20210212_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image3',
            field=models.ImageField(blank=True, null=True, upload_to='ECOM/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image4',
            field=models.ImageField(blank=True, null=True, upload_to='ECOM/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image5',
            field=models.ImageField(blank=True, null=True, upload_to='ECOM/images'),
        ),
    ]