# Generated by Django 4.0.6 on 2023-10-14 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itemmanager', '0017_remove_loan_customer_delete_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='loan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='itemmanager.loan'),
        ),
    ]
