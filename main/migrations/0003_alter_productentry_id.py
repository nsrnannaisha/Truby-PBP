# Generated by Django 5.1 on 2024-09-16 16:52

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_moodentry_productentry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productentry',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
