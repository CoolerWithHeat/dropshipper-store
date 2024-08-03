# Generated by Django 5.0.4 on 2024-05-31 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soothestore', '0041_alter_color_options_color_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment_Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=620)),
                ('completed', models.BooleanField(default=False)),
                ('verified_cart', models.JSONField(default={})),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
