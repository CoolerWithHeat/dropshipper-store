# Generated by Django 5.0.4 on 2024-07-02 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soothestore', '0060_subscribedcustomers_used_first_time_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment_session',
            name='associated_email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True),
        ),
    ]
