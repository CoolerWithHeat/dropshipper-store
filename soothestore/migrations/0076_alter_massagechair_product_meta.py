# Generated by Django 4.2.14 on 2024-08-15 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soothestore', '0075_alter_productmeta_og_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='massagechair',
            name='product_meta',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='soothestore.productmeta'),
        ),
    ]
