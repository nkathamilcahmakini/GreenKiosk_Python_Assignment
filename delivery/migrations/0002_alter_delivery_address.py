# Generated by Django 3.2.12 on 2023-07-08 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='address',
            field=models.CharField(max_length=255),
        ),
    ]