# Generated by Django 5.1.7 on 2025-03-26 18:47

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_username_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
