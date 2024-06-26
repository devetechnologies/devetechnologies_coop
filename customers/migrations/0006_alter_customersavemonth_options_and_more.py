# Generated by Django 4.2.13 on 2024-06-01 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_alter_customer_aportation_certify_amount_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customersavemonth',
            options={'verbose_name': 'Customer save', 'verbose_name_plural': 'Customers save'},
        ),
        migrations.AlterModelOptions(
            name='historicalcustomersavemonth',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Customer save', 'verbose_name_plural': 'historical Customers save'},
        ),
    ]
