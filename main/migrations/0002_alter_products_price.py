# Generated by Django 4.2.6 on 2023-10-21 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
    ]