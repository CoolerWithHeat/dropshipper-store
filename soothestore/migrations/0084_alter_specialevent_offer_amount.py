# Generated by Django 5.0.6 on 2024-09-19 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soothestore', '0083_specialevent_show_on_scroll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialevent',
            name='offer_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
