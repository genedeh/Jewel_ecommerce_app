# Generated by Django 3.2.6 on 2021-10-25 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0008_alter_jewelry_jewelry_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jewelry',
            name='jewelry_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='jewelries', to='Product.jewelry_type'),
        ),
    ]
