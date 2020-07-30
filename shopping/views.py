from django.shortcuts import render,get_object_or_404
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse


def homepage(request):
    return render(request,'homepage.html',{})

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponse(form.errors)
    else:
        form = ProductForm()
        context = {
            "form":form,
            "heading":"Create Product"
        }
        return render(request, "product/create_product.html", context)

@login_required
def list_product(request):
    products = Product.objects.filter(status=True)
    context = {
        "products":products,
        "heading":"List Products"
    }
    return render(request,"product/products.html",context)

@login_required
def view_product(request,pk):
    product = get_object_or_404(Product.objects.filter(pk=pk))
    context = {
        "product":product,
        "heading":"View Product"
    }
    return render(request,"product/product.html",context)

@login_required
def update_product(request,pk):
    instance = get_object_or_404(Product.objects.filter(pk=pk))
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

    else:
        form = ProductForm(instance=instance)
        context = {
            "form" : form,
            "heading":"Edit Product"
        }
        return render(request,"product/create_product.html",context)

# @login_required
# def delete_product(request,pk):
#     product = get_object_or_404(Product.objects.filter(pk=pk))
#     product.delete()
#     return HttpResponseRedirect("/")
