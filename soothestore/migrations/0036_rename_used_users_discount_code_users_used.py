# Generated by Django 5.0.4 on 2024-05-06 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soothestore', '0035_discount_code_used_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discount_code',
            old_name='used_users',
            new_name='users_used',
        ),
    ]
