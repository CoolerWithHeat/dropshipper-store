# Generated by Django 4.2.7 on 2024-03-19 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soothestore', '0015_massagechair_discount_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chairfeature',
            name='called',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='chairfeature',
            name='feature_description',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]