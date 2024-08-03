# Generated by Django 5.0.4 on 2024-05-06 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soothestore', '0034_subscribedcustomers'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount_code',
            name='used_users',
            field=models.ManyToManyField(related_name='customers_used_this_code', to='soothestore.subscribedcustomers'),
        ),
    ]
