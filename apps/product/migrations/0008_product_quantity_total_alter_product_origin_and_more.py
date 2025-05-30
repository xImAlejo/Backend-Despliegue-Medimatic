# Generated by Django 5.2 on 2025-05-29 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_product_bill_text_alter_product_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity_total',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='origin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='proyect',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
