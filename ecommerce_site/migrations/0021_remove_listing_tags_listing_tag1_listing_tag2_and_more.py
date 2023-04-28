# Generated by Django 4.1.7 on 2023-04-28 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_site', '0020_listing_buyorsell_tag_listing_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='tags',
        ),
        migrations.AddField(
            model_name='listing',
            name='tag1',
            field=models.CharField(default='false', max_length=30),
        ),
        migrations.AddField(
            model_name='listing',
            name='tag2',
            field=models.CharField(default='false', max_length=30),
        ),
        migrations.AddField(
            model_name='listing',
            name='tag3',
            field=models.CharField(default='false', max_length=30),
        ),
        migrations.AddField(
            model_name='listing',
            name='tag4',
            field=models.CharField(default='false', max_length=30),
        ),
        migrations.AddField(
            model_name='listing',
            name='tag5',
            field=models.CharField(default='false', max_length=30),
        ),
    ]