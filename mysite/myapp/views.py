from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    items = Product.objects.all()
    context = {
        'items': items
    }
    return render(request, "myapp/index.html", context)

# Create your views here.
def indexItem(request, myid):
    item = Product.objects.get(id=myid)
    context = {
        'item': item
    }
    return render(request, "myapp/detail.html", context=context)

