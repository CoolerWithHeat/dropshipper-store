# Generated by Django 5.0.4 on 2024-06-15 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soothestore', '0048_rename_payment_amount_payment_session_expected_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_session',
            name='expected_amount',
            field=models.FloatField(default=None),
        ),
    ]