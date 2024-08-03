# Generated by Django 5.0.4 on 2024-07-07 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soothestore', '0064_customerinquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chairreview',
            name='review_text',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='customerinquiry',
            name='customer_email',
            field=models.EmailField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='customerinquiry',
            name='customer_name',
            field=models.CharField(default=None, max_length=60),
        ),
    ]
