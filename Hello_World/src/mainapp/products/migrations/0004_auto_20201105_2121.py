# Generated by Django 3.1.2 on 2020-11-06 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20201026_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='type',
            field=models.CharField(choices=[('Ms.', 'Ms.'), ('Mrs.', 'Mrs.'), ('Mr.', 'Mr.')], max_length=60),
        ),
    ]