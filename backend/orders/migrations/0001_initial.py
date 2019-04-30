# Generated by Django 2.2 on 2019-04-30 19:44

from django.db import migrations, models
import django.db.models.deletion
import orders.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(default=orders.models.generateUUID, max_length=36, unique=True)),
                ('status', models.CharField(choices=[('created', 'Created'), ('paid', 'Paid'), ('shipped', 'Shipped'), ('refunded', 'Refunded')], default='created', max_length=120)),
                ('subtotal', models.DecimalField(decimal_places=2, default=5.99, max_digits=100)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('products', models.ManyToManyField(blank=True, to='products.Product')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
            ],
        ),
    ]
