# Generated by Django 5.1.6 on 2025-03-19 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inflows', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inflow',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='inflow',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
