# Generated by Django 5.1.3 on 2025-01-16 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ensemble', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ensemble',
            name='organization',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=60),
        ),
    ]
