# Generated by Django 2.2 on 2019-05-11 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20190511_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to='profiles.Profile'),
        ),
    ]