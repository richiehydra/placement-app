# Generated by Django 4.1.3 on 2022-12-20 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_rename_price_order_cgpa_rename_product_order_company_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='profile',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='student',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='cgpa',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='company',
            new_name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
