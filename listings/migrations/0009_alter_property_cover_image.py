# Generated by Django 5.1.7 on 2025-03-25 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_alter_property_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='cover_image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
    ]
