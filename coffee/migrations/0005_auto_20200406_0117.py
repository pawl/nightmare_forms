# Generated by Django 3.0.5 on 2020-04-06 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0004_auto_20200406_0104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttea',
            name='default_quantity',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='base price of the product, does not include cost of size increases', max_digits=4),
        ),
    ]
