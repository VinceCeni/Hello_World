# Generated by Django 3.1.2 on 2021-02-01 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0017_auto_20210201_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='type',
            field=models.CharField(blank=True, choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.')], default='', max_length=60),
        ),
    ]
