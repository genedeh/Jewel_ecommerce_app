# Generated by Django 3.2.6 on 2021-10-22 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_alter_jewelry_type_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jewelry',
            name='price',
            field=models.FloatField(help_text='Currency in naira'),
        ),
        migrations.AlterField(
            model_name='jewelry',
            name='video',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
