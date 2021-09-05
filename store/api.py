from rest_framework.response import Response
from store.models import Item, ItemInStock, ItemVariant, ShoppingCart, OrderItem, SIZE_CHOISES, COLOR_CHOISES
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import random

from .serializers import ItemSerializers, ItemInStockSerializers, ShoppingCartSerializers


class OneShotApi(APIView):

    def get(self, request):

        item = Item.objects.all()
        ItemVariant.objects.all().delete()
        for item in item:
            index = random.sample(range(len(COLOR_CHOISES)), 4)
            for ind in list(index):
                ItemVariant.objects.create(color=COLOR_CHOISES[ind][0], item=item)

        items_variants = ItemVariant.objects.all()
        ItemInStock.objects.all().delete()
        for item in items_variants:
            for size in SIZE_CHOISES:
                ItemInStock.objects.create(size=size[0], quantity=100, item_variant=item)
        return Response("ok")



class ItemsListApi(APIView):

    def get(self, request):
        if request.query_params['category'] == 'All':
            items = Item.objects.filter(gender=request.query_params['gender'])
        else:
            items = Item.objects.filter(gender=request.query_params['gender'], category=request.query_params['category'])
        serializer = ItemSerializers(items, many=True)
        return Response({"items": serializer.data})

class ItemsInStockApi(APIView):

    def get(self, request):
        item_variant = ItemVariant.objects.get(id=request.query_params['variant_id'])
        items_in_stock = ItemInStock.objects.filter(item_variant=item_variant)
        serializer = ItemInStockSerializers(items_in_stock, many=True)
        return Response({"items_in_stock": serializer.data})


class ShoppingCartApi(APIView):

    def post(self, request):
        username = request.user
        try:
            shopping_cart = ShoppingCart.objects.get(user__username=username)
        except:
            shopping_cart = ShoppingCart.objects.create(user=User.objects.get(username=username))
        item = get_object_or_404(ItemInStock, id=request.data.get('item_id'))
        try:
            order_item = shopping_cart.order_items.get(item=item)
            if order_item.quantity == order_item.item.quantity:
                return Response("out_of_stock")
            else:
                order_item.quantity += 1
                order_item.save()
        except:
            shopping_cart.order_items.add(OrderItem.objects.create(item=item))
        return Response("ok")

    def get(self, request):
        username = request.user
        try:
            shopping_cart = ShoppingCart.objects.get(user__username=username)
        except:
            shopping_cart = ShoppingCart.objects.create(user=User.objects.get(username=username))
        serializer = ShoppingCartSerializers(shopping_cart)
        return Response({"shopping_cart": serializer.data})

class OrderItemApi(APIView):

    def post(self, request):
        username = request.user
        shopping_cart = ShoppingCart.objects.get(user__username=username)
        order_item = shopping_cart.order_items.get(id=request.data.get('order_item_id'))
        quantity = request.data.get('quantity')
        if int(quantity) == 0:
            order_item.delete()
        else:
            order_item.quantity = quantity
            order_item.save()
        return Response("ok")

class PurchaseApi(APIView):

    def post(self, request):
        username = request.user
        shopping_cart = ShoppingCart.objects.get(user__username=username)
        for order_item in shopping_cart.order_items.all():
            order_item.item.quantity -= order_item.quantity
            if order_item.item.quantity <= 0:
                order_item.item.delete()
            else:
                order_item.item.save()
            order_item.delete()
        return Response("ok")


