# Generated by Django 5.0.4 on 2024-06-16 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soothestore', '0049_alter_payment_session_expected_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment_session',
            name='tracking_available',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
