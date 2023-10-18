# Generated by Django 4.0.6 on 2023-10-17 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itemmanager', '0022_esection_expense_esection'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('incsection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='itemmanager.incsection')),
            ],
        ),
    ]