# Generated by Django 4.1.3 on 2025-03-02 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_rename_price_application_cgpa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='product',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='customer',
            new_name='student',
        ),
    ]
