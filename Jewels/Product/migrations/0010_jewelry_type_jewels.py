# Generated by Django 3.2.6 on 2021-10-25 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0009_alter_jewelry_jewelry_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='jewelry_type',
            name='jewels',
            field=models.ManyToManyField(related_name='jewelries', to='Product.Jewelry'),
        ),
    ]