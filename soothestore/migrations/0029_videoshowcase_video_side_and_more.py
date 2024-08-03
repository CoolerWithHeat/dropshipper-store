# Generated by Django 5.0.4 on 2024-04-30 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soothestore', '0028_alter_videoshowcase_showcase_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoshowcase',
            name='video_side',
            field=models.CharField(choices=[('any side', 'any side'), ('left', 'left'), ('right', 'right')], default='any side', max_length=35),
        ),
        migrations.AlterField(
            model_name='videoshowcase',
            name='showcase_text',
            field=models.TextField(blank=True, default=None, max_length=580, null=True),
        ),
    ]
