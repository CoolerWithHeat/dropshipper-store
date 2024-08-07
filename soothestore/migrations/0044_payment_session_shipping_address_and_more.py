# Generated by Django 5.0.4 on 2024-06-15 06:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soothestore', '0043_shippinginformation'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment_session',
            name='shipping_address',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='soothestore.shippinginformation'),
        ),
        migrations.AlterField(
            model_name='payment_session',
            name='verified_cart',
            field=models.JSONField(default=dict),
        ),
    ]
