# Generated by Django 3.1.2 on 2020-11-07 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profiles_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='type',
            field=models.CharField(blank=True, choices=[('Mr.', 'Mr.'), ('Ms.', 'Ms.'), ('Mrs.', 'Mrs.')], default='', max_length=60),
        ),
    ]
