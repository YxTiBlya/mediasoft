# Generated by Django 4.0.4 on 2022-06-21 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_shop_alter_city_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shop',
            options={'verbose_name': 'Магазин', 'verbose_name_plural': 'Магазины'},
        ),
    ]