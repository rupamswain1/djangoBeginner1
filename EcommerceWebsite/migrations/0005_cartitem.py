# Generated by Django 3.1.2 on 2020-11-22 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcommerceWebsite', '0004_auto_20201121_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cutomer_id', models.CharField(max_length=100)),
                ('product_id', models.IntegerField()),
                ('product_quantity', models.IntegerField()),
            ],
        ),
    ]
