# Generated by Django 5.0.4 on 2024-06-16 16:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soothestore', '0053_alter_brand_order_tracking_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number_provided_by_brand', models.CharField(default='order number actual brand provides', max_length=25)),
                ('tracking_stage', models.CharField(choices=[(1, 'Order Confirmed'), (2, 'Processing'), (3, 'On the way'), (4, 'Delivered')], default=1, max_length=25)),
                ('of_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soothestore.payment_session')),
                ('tracking_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soothestore.massagechair')),
            ],
        ),
    ]
