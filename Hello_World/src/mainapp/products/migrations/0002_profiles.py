# Generated by Django 3.1.2 on 2020-10-26 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, default='', max_length=60)),
                ('lastname', models.CharField(blank=True, default='', max_length=60)),
                ('Email', models.CharField(blank=True, default='', max_length=60)),
                ('username', models.CharField(blank=True, default='', max_length=60)),
            ],
        ),
    ]