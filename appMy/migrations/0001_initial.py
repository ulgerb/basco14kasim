# Generated by Django 4.1.4 on 2023-01-11 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, verbose_name='Kategori')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('text', models.TextField(verbose_name='Açıklama')),
                ('price', models.FloatField(verbose_name='Ürün Fiyatı')),
                ('image', models.FileField(upload_to='', verbose_name='Ürün Fotoğrafı')),
                ('stok', models.IntegerField(verbose_name='Ürün Stok')),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appMy.category', verbose_name='Kategori')),
            ],
        ),
    ]
