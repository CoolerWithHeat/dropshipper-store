# Generated by Django 5.0.4 on 2024-07-01 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soothestore', '0059_alter_subscribedcustomers_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribedcustomers',
            name='used_first_time_discount',
            field=models.BooleanField(default=False),
        ),
    ]
