from django.shortcuts import render, redirect
from django.views import View
from .models import Item, ItemInStock, ItemVariant, ShoppingCart
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, View):

    def get(self, request):
        return redirect('items_list_view')

class ItemsListView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'store/items_list.html')


class ItemDetailView(LoginRequiredMixin, View):

    def get(self, request, slug):
        item = Item.objects.get(slug=slug)
        item_variants = ItemVariant.objects.filter(item=item)
        return render(request, 'store/item_detail.html', {'item': item, 'item_variants': item_variants})


class ShoppingCartView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'store/shopping_cart.html')


