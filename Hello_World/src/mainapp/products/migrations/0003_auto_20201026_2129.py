# Generated by Django 3.1.2 on 2020-10-27 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_profiles'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='products',
        ),
        migrations.DeleteModel(
            name='Profiles',
        ),
    ]