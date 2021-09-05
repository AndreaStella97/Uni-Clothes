from django.contrib import admin
from .models import Item, ItemVariant, ItemInStock, ShoppingCart, OrderItem

admin.site.register(Item)
admin.site.register(ItemVariant)
admin.site.register(ItemInStock)
admin.site.register(ShoppingCart)
admin.site.register(OrderItem)
