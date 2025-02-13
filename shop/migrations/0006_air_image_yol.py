# Generated by Django 5.0.6 on 2024-05-20 08:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_remove_air_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='air',
            name='image',
            field=models.ImageField(null=True, upload_to='air_image/'),
        ),
        migrations.CreateModel(
            name='Yol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='yol_image/')),
                ('air', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yoll', to='shop.air')),
            ],
        ),
    ]
