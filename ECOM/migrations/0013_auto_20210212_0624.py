# Generated by Django 3.1.5 on 2021-02-12 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ECOM', '0012_auto_20210212_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image2',
            field=models.ImageField(blank=True, null=True, upload_to='ECOM/images'),
        ),
    ]
