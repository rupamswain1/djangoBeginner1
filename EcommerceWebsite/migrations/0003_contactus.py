# Generated by Django 3.1.2 on 2020-11-21 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcommerceWebsite', '0002_auto_20201115_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phoneNumber', models.IntegerField(max_length=13)),
                ('email', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=5000)),
                ('subject', models.CharField(max_length=500)),
            ],
        ),
    ]
