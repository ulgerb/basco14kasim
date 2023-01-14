from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .models import *
from django.contrib.auth.models import User

def index(request):
    
    return render(request,'index.html')

def Products(request):
    products = Product.objects.all()
    context = {"products": products}
    
    return render(request,'products.html',context)

def Detail(request,id):
    product = get_object_or_404(Product, id=id)
    context = {"product": product}
    if request.method == 'POST':
        adet = int(request.POST['adet'])
        fiyat = product.price * adet
        try:
            if adet <= product.stok:
                if Shoping.objects.filter(product=product, user=request.user).exists():
                    shoping = Shoping.objects.filter(user=request.user).get(product=product)
                    if (shoping.adet + adet) <= product.stok:
                        
                        
                        shoping.adet += adet 
                        shoping.fiyat += fiyat
                        shoping.save()
                        return HttpResponseRedirect('/detail/{}/'.format(id))
                    else:
                        shoping.adet = product.stok
                        shoping.fiyat = product.stok * product.price
                        shoping.save()
                        context.update({"hata": "Sepetinizde stok sayısını aştınız"})
                else:    
                    shoping = Shoping(user = request.user , product=product, adet=adet,fiyat=fiyat)
                    shoping.save()
                    return HttpResponseRedirect('/detail/{}/'.format(id))
            else:
                context.update({ "hata" : "Stok sayısını aştınız!" })
        except:
            pass
        
    
    
    return render(request,'detail.html',context)

def ShopingUser(request):
    shops = Shoping.objects.filter(user=request.user)
    toplam = 0

    
    
    if request.method == "POST":
        adet = int(request.POST["adet"])
        product_id = request.POST["product-id"]
        product = shops.get(id=product_id)
        product.adet = adet
        product.fiyat = adet * product.product.price
        product.save()
        return redirect('Shoping')
    
    for i in shops:
        toplam += i.fiyat
    
    context={
        "shops": shops,
        "toplam": toplam,
    }
    return render(request,'shoping.html',context)

def ShopingDelete(request,id):
    shop = Shoping.objects.get(id=id)
    shop.delete()
    return redirect('Shoping')

def About(request):
    
    return render(request,'about.html')

def Services(request):
    
    return render(request,'services.html')

def Contact(request):
    
    return render(request,'contact.html')

