# Generated by Django 4.1.7 on 2023-04-26 23:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerce_site', '0014_alter_chat_user_alter_listing_seller_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profilel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chats', models.ManyToManyField(related_name='chats', to='ecommerce_site.chat')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]