# Generated by Django 5.0.4 on 2024-07-23 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soothestore', '0068_user_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='CustomUser',
        ),
    ]
