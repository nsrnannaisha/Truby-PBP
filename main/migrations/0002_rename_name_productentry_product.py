# Generated by Django 5.1.1 on 2024-10-07 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productEntry',
            old_name='name',
            new_name='product',
        ),
    ]