# Generated by Django 3.2.6 on 2021-10-22 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Product', '0006_alter_jewelry_jewelry_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('jewelry', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Product.jewelry')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Product.jewelry')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180)),
                ('order_item', models.ManyToManyField(to='customers.OrderItem')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('image', models.ImageField(blank=True, default='/no_profile_image.jpg', upload_to='')),
                ('password', models.CharField(max_length=8, unique=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.order')),
                ('wishlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.wishlist')),
            ],
        ),
    ]
