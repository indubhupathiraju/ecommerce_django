# Generated by Django 3.1.5 on 2021-02-17 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ECOM', '0016_remove_address_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='Payment',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='orders',
            name='Status',
            field=models.CharField(default='', max_length=50),
        ),
    ]