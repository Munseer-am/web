# Generated by Django 4.0.6 on 2022-07-28 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rashik', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='bold',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='image',
            name='text',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
