# Generated by Django 3.1.2 on 2021-01-06 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_auto_20201115_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='type',
            field=models.CharField(blank=True, choices=[('Ms.', 'Ms.'), ('Mr.', 'Mr.'), ('Mrs.', 'Mrs.')], default='', max_length=60),
        ),
    ]
