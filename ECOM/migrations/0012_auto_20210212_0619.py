# Generated by Django 3.1.5 on 2021-02-12 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ECOM', '0011_auto_20210212_0504'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_image',
            new_name='product_image1',
        ),
        migrations.AddField(
            model_name='product',
            name='product_image2',
            field=models.ImageField(null=True, upload_to='ECOM/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image3',
            field=models.ImageField(null=True, upload_to='ECOM/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image4',
            field=models.ImageField(null=True, upload_to='ECOM/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image5',
            field=models.ImageField(null=True, upload_to='ECOM/images'),
        ),
    ]
