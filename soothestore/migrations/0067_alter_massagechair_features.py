# Generated by Django 5.0.4 on 2024-07-14 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soothestore', '0066_payment_session_order_closed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='massagechair',
            name='features',
            field=models.ManyToManyField(blank=True, related_name='Massage_Features', to='soothestore.chairfeature'),
        ),
    ]
