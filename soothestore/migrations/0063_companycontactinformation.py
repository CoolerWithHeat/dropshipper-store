# Generated by Django 5.0.4 on 2024-07-05 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soothestore', '0062_massagechair_has_reviewers'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyContactInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, default=None, max_length=25)),
                ('company_email', models.EmailField(blank=True, default=None, max_length=255)),
            ],
        ),
    ]
