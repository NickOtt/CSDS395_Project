# Generated by Django 4.1.7 on 2023-03-07 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_site', '0007_remove_listing_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.FileField(default='', upload_to=''),
        ),
    ]