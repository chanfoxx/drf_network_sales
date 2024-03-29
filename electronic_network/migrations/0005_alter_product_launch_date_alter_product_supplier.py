# Generated by Django 5.0.3 on 2024-03-14 04:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronic_network', '0004_alter_contact_email_alter_contact_house_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='launch_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата выхода'),
        ),
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='electronic_network.supplier', verbose_name='Поставщик'),
        ),
    ]
