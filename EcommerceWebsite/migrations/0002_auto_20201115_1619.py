# Generated by Django 3.1.2 on 2020-11-15 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcommerceWebsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='', upload_to='media'),
        ),
    ]
