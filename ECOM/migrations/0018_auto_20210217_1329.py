# Generated by Django 3.1.5 on 2021-02-17 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ECOM', '0017_auto_20210217_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='Status',
            field=models.CharField(default='Pending', max_length=50),
        ),
    ]
