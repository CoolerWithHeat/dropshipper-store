# Generated by Django 4.2.7 on 2024-03-13 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soothestore', '0010_chairreview_customer_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='chairfeature',
            name='feature_description',
            field=models.CharField(blank=True, default=None, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='chairfeature',
            name='feature_showcase',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='chairfeature',
            name='called',
            field=models.CharField(default=None, max_length=20),
        ),
    ]