from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

SIZE_CHOISES = (("XXS", "XXS"), ("XS", "XS"), ("S", "S"), ("M", "M"), ("L", "L"), ("XL", "XL"), ("XXL", "XXL"))
COLOR_CHOISES = (("blue", "Blue"), ("red", "Red"), ("green", "Green"), ("yellow", "Yellow"), ("brown", "Brown"), ("orange", "Orange"),
                     ("pink", "Pink"), ("black", "Black"), ("white", "White"), ("grey", "Grey"), ("purple", "Purple"))

class Item(models.Model):

    CATEGORY_CHOISES = (("T-Shirt", "T-Shirt"), ("Shirt", "Shirt"), ("Sweater", "Sweater"), ("Sweatshirt", "Sweatshirt"),
                        ("Jeans", "Jeans"), ("Pants", "Pants"), ("Jacket", "Jacket"), ("Socks", "Socks"))

    GENDER_CHOISES = (("Man", "Man"), ("Woman", "Woman"))

    category = models.CharField(max_length=20,
                                choices=CATEGORY_CHOISES)
    gender = models.CharField(max_length=10,
                              choices=GENDER_CHOISES)
    brand = models.CharField(max_length=50)
    description = models.TextField(max_length=3000, null=True)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.category + " " + self.brand + " " + self.gender

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category + "-" + self.brand + "-" + self.gender + "-" + str(self.id))
        return super(Item, self).save(*args, **kwargs)



class ItemVariant(models.Model):

    color = models.CharField(max_length=10, choices=COLOR_CHOISES)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.__str__() + " " + self.color

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['color', 'item'], name='variant')
        ]


class ItemInStock(models.Model):

    size = models.CharField(max_length=5, choices=SIZE_CHOISES)
    quantity = models.IntegerField()
    item_variant = models.ForeignKey(ItemVariant, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_variant.__str__() + " " + self.size

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['size', 'item_variant'], name='size_details')
        ]

class OrderItem(models.Model):

    item = models.ForeignKey(ItemInStock, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.item.__str__() + " " + str(self.id)

    @property
    def itemBrand(self):
        return self.item.item_variant.item.brand

    @property
    def itemCategory(self):
        return self.item.item_variant.item.category

    @property
    def itemGender(self):
        return self.item.item_variant.item.gender

    @property
    def itemSize(self):
        return self.item.size

    @property
    def itemColor(self):
        return self.item.item_variant.color

    @property
    def itemSlug(self):
        return self.item.item_variant.item.slug

    @property
    def quantityInStock(self):
        return self.item.quantity

    @property
    def itemImage(self):
        return self.item.item_variant.item.image

    @property
    def price(self):
        return round(self.item.item_variant.item.price * self.quantity, 2)


class ShoppingCart(models.Model):

    order_items = models.ManyToManyField(OrderItem)
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)

    @property
    def totalPrice(self):
        total = 0
        for item in self.order_items.all():
            total += item.price
        return round(total, 2)

