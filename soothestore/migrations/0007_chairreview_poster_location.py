# Generated by Django 4.2.7 on 2024-03-13 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soothestore', '0006_rename_chaircomment_chairreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='chairreview',
            name='poster_location',
            field=models.CharField(blank=True, default=None, max_length=35, null=True),
        ),
    ]