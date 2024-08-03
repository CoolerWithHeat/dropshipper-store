# Generated by Django 5.0.4 on 2024-05-06 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soothestore', '0033_alter_discount_code_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribedCustomers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=120, null=True)),
                ('email', models.EmailField(max_length=60)),
            ],
        ),
    ]