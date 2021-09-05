from rest_framework import serializers


class ItemSerializers(serializers.Serializer):
    category = serializers.CharField(max_length=20)
    gender = serializers.CharField(max_length=10)
    brand = serializers.CharField(max_length=50)
    price = serializers.FloatField()
    image = serializers.ImageField()
    slug = serializers.SlugField()

class ItemInStockSerializers(serializers.Serializer):
    id = serializers.CharField()
    size = serializers.CharField(max_length=5)
    quantity = serializers.IntegerField()

class OrderItemSerializer(serializers.Serializer):
    id = serializers.CharField()
    itemBrand = serializers.CharField()
    itemCategory = serializers.CharField()
    itemGender = serializers.CharField()
    itemSize = serializers.CharField()
    itemColor = serializers.CharField()
    itemImage = serializers.ImageField()
    itemSlug = serializers.SlugField()
    quantityInStock = serializers.IntegerField()
    quantity = serializers.IntegerField()
    price = serializers.FloatField()

class ShoppingCartSerializers(serializers.Serializer):
    order_items = OrderItemSerializer(many=True)
    totalPrice = serializers.FloatField()


