# Generated by Django 5.1.7 on 2025-03-22 06:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_user'),
        ('listings', '0003_rename_cover_image_propertyimage_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='host',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='accounts.profile'),
        ),
    ]
