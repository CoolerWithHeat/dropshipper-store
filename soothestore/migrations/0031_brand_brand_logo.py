# Generated by Django 5.0.4 on 2024-05-06 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soothestore', '0030_alter_massagechair_additional_images_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='brand_logo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
