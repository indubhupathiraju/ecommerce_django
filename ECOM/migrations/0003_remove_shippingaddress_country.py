# Generated by Django 3.1.5 on 2021-02-10 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ECOM', '0002_shippingaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='country',
        ),
    ]
