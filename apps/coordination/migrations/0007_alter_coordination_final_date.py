# Generated by Django 5.2 on 2025-04-14 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordination', '0006_remove_coordination_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordination',
            name='final_date',
            field=models.DateField(blank=True, null=True, verbose_name='Final Date'),
        ),
    ]
