from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category,Air
from .forms import CreateProduct
def home(request):
    products = Product.objects.all()
    categorys = Category.objects.all()
    air = Air.objects.all()
    return render(request, 'home.html', {"products":products, "cats":categorys, 'air':air})

def category(request, id):
    cat = get_object_or_404(Category, id=id)
    products = cat.products.all()
    categorys = Category.objects.all()
    air = Air.objects.all()
    return render(request, 'home.html', {"products": products, "cats":categorys, 'air':air})

def batafsil(request, id):
    product = get_object_or_404(Product, id=id)
    categorys = Category.objects.all()
    air = Air.objects.all()
    return render(request, 'batafsil.html', {"product": product, "cats": categorys, 'air':air})

def create_product(request):
    form = CreateProduct()
    if request.method == "POST":
        form = CreateProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'create_product.html', {"form":form})

def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    form = CreateProduct(instance=product)
    if request.method == "POST":
        form = CreateProduct(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('batafsil', id=product.id)
    return render(request, 'create_product.html', {"form": form})

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('/')


def res(request):
    air = Air.objects.all()
    categorys = Category.objects.all()
    return render(request, 'base.html', {"air": air, "cats": categorys})



def yol(request, id):
    air = get_object_or_404(Air, id=id)
    yol = air.yoll.all()
    air = Air.objects.all()
    category = Category.objects.all()
    return render(request, 'yol.html', context={'yol':yol, 'air':air, 'cats':category})