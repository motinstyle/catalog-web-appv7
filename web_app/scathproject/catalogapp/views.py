from django.shortcuts import render
from django.http import HttpResponse
from .models import products, UserCards

# Create your views here.
def catalog_index(request):
    # return HttpResponse("<h4>Catalog</h4>")
    cards = products.objects.all()
    return render(request, 'catalogapp/catalog_index.html', {'cards' : cards})

def inventory_index(request):
    # return HttpResponse("<h4>Inventory</h4>")
    user_cards = UserCards.objects.all()
    return render(request, 'catalogapp/inventory_index.html', {'user_cards' : user_cards})