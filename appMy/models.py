from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category = models.CharField(("Kategori"), max_length=50)
    
    def __str__(self):
        return self.category

class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE, null=True)
    title = models.CharField(("Başlık"), max_length=50)
    text = models.TextField(("Açıklama"))
    price = models.FloatField(("Ürün Fiyatı"))
    image = models.FileField(("Ürün Fotoğrafı"), upload_to='', max_length=100)
    stok = models.IntegerField(("Ürün Stok"))

    def __str__(self):
        return self.title

class Shoping(models.Model):
    # kullanıcı bilgisi, ürün, adet, fiyat, 
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
    adet = models.IntegerField(("Adet"))
    fiyat = models.FloatField(("Toplam Fiyat"))
    