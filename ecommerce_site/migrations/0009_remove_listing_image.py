# Generated by Django 4.1.7 on 2023-03-07 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_site', '0008_listing_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='image',
        ),
    ]
