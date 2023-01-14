# Generated by Django 4.1.4 on 2023-01-13 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appMy', '0002_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shoping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adet', models.IntegerField(verbose_name='Adet')),
                ('fiyat', models.FloatField(verbose_name='Toplam Fiyat')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMy.product', verbose_name='Ürün')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
    ]