from decimal import Decimal

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone


class EspressoShot(models.Model):
    """
    Allows adding new types of espresso shots through the database
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ProductEspressoShot(models.Model):
    """
    Intermediate model for Product <-> EspressoShot, for Product.allowed_espresso_shots

    Stores additional info for the Product's EspressoShot
    """
    espresso_shot = models.ForeignKey(EspressoShot, on_delete=models.PROTECT)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    default_quantity = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)


class OrderItemProductEspressoShot(models.Model):
    """
    Intermediate model for OrderItem <-> ProductEspressoShot, stores quantity

    Allows an OrderItem to have multiple types of EspressoShots with their own quantity
    """
    product_espresso_shot = models.ForeignKey(ProductEspressoShot, on_delete=models.PROTECT)
    quantity = models.IntegerField()


class Sweetener(models.Model):
    """
    Allows adding new types of sweeteners through the database
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ProductSweetener(models.Model):
    """
    Intermediate model for Product <-> Sweetener, for Product.allowed_sweeteners

    Stores additional info for the Product's Sweetener
    """
    sweetener = models.ForeignKey(Sweetener, on_delete=models.PROTECT)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    default_quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)


class OrderItemProductSweetener(models.Model):
    """
    Intermediate model for OrderItem <-> ProductSweetener, stores quantity

    Allows an OrderItem to have multiple types of Sweeteners with their own quantity
    """
    product_sweetener = models.ForeignKey(ProductSweetener, on_delete=models.PROTECT)
    quantity = models.IntegerField()


class Size(models.Model):
    """
    Allows adding new sizes through the database
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ProductSize(models.Model):
    """
    Intermediate model for Product <-> Size, for Product.allowed_sizes/default_size

    Stores additional info (including pricing) for the Product's Size
    """
    size = models.ForeignKey(Size, on_delete=models.PROTECT)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    price = models.DecimalField(default=0, max_digits=4, decimal_places=2)
    # pumps of sauce and syrup for the product size
    flavor_pumps = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    # default sizes are set on Product


class Milk(models.Model):
    """
    Allows adding new types of milks through the database
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class TempChoice(models.Model):
    """
    Stores choices for ProductMilk temperatures

    Allows adding and renaming ProductMilk temp options through the database
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class FoamChoice(models.Model):
    """
    Stores choices for ProductMilk foam

    Allows adding and renaming ProductMilk foam options through the database
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ProductMilk(models.Model):
    """
    Intermediate model for Product <-> Milk, for Product.allowed_milks/default_milk

    Stores additional info (including temperature, foam, and pricing) for the Product's Milk
    """
    default_temp = models.ForeignKey(
        TempChoice,
        on_delete=models.PROTECT,
        related_name='default_product_milks',
        null=True)
    allowed_temps = models.ManyToManyField(TempChoice)

    default_foam = models.ForeignKey(
        FoamChoice,
        on_delete=models.PROTECT,
        related_name='default_product_milks',
        null=True)
    allowed_foams = models.ManyToManyField(FoamChoice)

    milk = models.ForeignKey(Milk, on_delete=models.PROTECT)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    price = models.DecimalField(default=0, max_digits=4, decimal_places=2)
    is_active = models.BooleanField(default=True)
    # default milk is set on Product


class Juice(models.Model):
    """
    Allows adding new types of juices through the database
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ProductJuice(models.Model):
    """
    Intermediate model for Product <-> Juice, for Product.allowed_juices/default_juice

    Stores additional info (including pricing) for the Product's Juice
    """
    juice = models.ForeignKey(Juice, on_delete=models.PROTECT)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    price = models.DecimalField(default=0, max_digits=4, decimal_places=2)
    is_active = models.BooleanField(default=True)
    is_default = models.BooleanField(default=False)


class OrderItemProductJuice(models.Model):
    """
    Intermediate model for OrderItem <-> ProductJuice, stores quantity

    Allows an OrderItem to have multiple types of Juice with their own quantity
    """
    product_juice = models.ForeignKey(ProductJuice, on_delete=models.PROTECT)
    quantity = models.IntegerField()


class FlavorCategory(models.Model):
    """
    Used for labels on sections of flavors
    """
    class Meta:
        verbose_name_plural = "Flavor Categories"

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Flavor(models.Model):
    """
    Allows adding new types of flavors through the database
    """
    category = models.ForeignKey(FlavorCategory, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ProductFlavor(models.Model):
    """
    Intermediate model for Product <-> Flavor, for Product.allowed_flavors/default_flavor

    Stores additional info (including pricing) for the Product's Flavor
    """
    flavor = models.ForeignKey(Flavor, on_delete=models.PROTECT)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    price = models.DecimalField(default=0, max_digits=4, decimal_places=2)
    is_active = models.BooleanField(default=True)
    is_default = models.BooleanField(default=False)


class OrderItemProductFlavor(models.Model):
    """
    Intermediate model for OrderItem <-> ProductFlavor, stores quantity

    Allows an OrderItem to have multiple types of Flavor with their own quantity
    """
    product_flavor = models.ForeignKey(ProductFlavor, on_delete=models.PROTECT)
    quantity = models.IntegerField()


class ToppingCategory(models.Model):
    """
    Used for labels on sections of toppings
    """
    class Meta:
        verbose_name_plural = "Topping Categories"

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ToppingChoice(models.Model):
    """
    Stores choices for amounts of Toppings

    Allows adding and renaming topping amount options through the database
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Topping(models.Model):
    """
    Allows adding new types of toppings through the database
    """
    default_choice = models.ForeignKey(
        ToppingChoice,
        on_delete=models.PROTECT,
        related_name='default_toppings',
        null=True)
    allowed_choices = models.ManyToManyField(ToppingChoice)
    category = models.ForeignKey(ToppingCategory, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ProductTopping(models.Model):
    """
    Intermediate model for Product <-> Topping, for Product.allowed_toppings/default_toppings

    Stores additional info (including pricing) for the Product's Topping
    """
    topping = models.ForeignKey(Topping, on_delete=models.PROTECT)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    price = models.DecimalField(default=0, max_digits=4, decimal_places=2)
    is_active = models.BooleanField(default=True)
    is_default = models.BooleanField(default=False)


class OrderItemProductTopping(models.Model):
    """
    Intermediate model for OrderItem <-> ProductTopping, stores quantity

    Allows an OrderItem to have multiple types of Topping with their own quantity
    """
    product_topping = models.ForeignKey(ProductTopping, on_delete=models.PROTECT)
    quantity = models.IntegerField()


class Tea(models.Model):
    """
    Allows adding new types of teas through the database
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ProductTea(models.Model):
    """
    Intermediate model for Product <-> Tea, for Product.allowed_teas/default_teas

    Stores additional pricing info for the Product's Tea
    """
    topping = models.ForeignKey(Tea, on_delete=models.PROTECT)
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    price = models.DecimalField(default=0, max_digits=4, decimal_places=2)
    is_active = models.BooleanField(default=True)
    is_default = models.BooleanField(default=False)
    default_quantity = models.IntegerField()


class OrderItemProductTea(models.Model):
    """
    Intermediate model for OrderItem <-> ProductTea, stores quantity

    Allows an OrderItem to have multiple types of Tea with their own quantity
    """
    product_tea = models.ForeignKey(ProductTea, on_delete=models.PROTECT)
    quantity = models.IntegerField()


class IceChoice(models.Model):
    """
    Stores choices for Product ice levels

    Allows adding and renaming ice level options through the database
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class RoomChoice(models.Model):
    """
    Stores choices for Product room levels

    Allows adding and renaming room level options through the database
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Stores the allowed and default ingredients for a menu product, like a recipe
    but with the allowed modifications too.
    """
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    allowed_ice = models.ManyToManyField(IceChoice)
    default_ice = models.ForeignKey(
        IceChoice,
        on_delete=models.PROTECT,
        related_name='default_products',
        null=True)

    allowed_room = models.ManyToManyField(RoomChoice)
    default_room = models.ForeignKey(
        RoomChoice,
        on_delete=models.PROTECT,
        related_name='default_products',
        null=True)

    allowed_milks = models.ManyToManyField(Milk, through=ProductMilk)
    default_milk = models.ForeignKey(
        ProductMilk,
        on_delete=models.PROTECT,
        related_name='default_products',
        null=True)

    allowed_sizes = models.ManyToManyField(Size, through=ProductSize)
    default_size = models.ForeignKey(
        ProductSize,
        on_delete=models.PROTECT,
        related_name='default_products',
        null=True)

    allowed_sweeteners = models.ManyToManyField(Sweetener, through=ProductSweetener)
    default_sweeteners = models.ManyToManyField(ProductSweetener, related_name='default_products')

    allowed_espresso_shots = models.ManyToManyField(EspressoShot, through=ProductEspressoShot)
    default_espresso_shots = models.ManyToManyField(ProductEspressoShot, related_name='default_products')

    allowed_juices = models.ManyToManyField(Juice, through=ProductJuice)
    default_juices = models.ManyToManyField(ProductJuice, related_name='default_products')

    allowed_toppings = models.ManyToManyField(Topping, through=ProductTopping)
    default_toppings = models.ManyToManyField(ProductTopping, related_name='default_products')

    allowed_teas = models.ManyToManyField(Tea, through=ProductTea)
    default_teas = models.ManyToManyField(ProductTea, related_name='default_products')

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    total = models.DecimalField(default=0, max_digits=4, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    ice = models.ForeignKey(IceChoice, on_delete=models.PROTECT)
    room = models.ForeignKey(RoomChoice, on_delete=models.PROTECT)
    size = models.ForeignKey(ProductSize, on_delete=models.PROTECT)
    milk = models.ForeignKey(ProductMilk, on_delete=models.PROTECT)

    sweeteners = models.ManyToManyField(OrderItemProductSweetener)
    espresso_shots = models.ManyToManyField(OrderItemProductEspressoShot)
    toppings = models.ManyToManyField(OrderItemProductTopping)
    flavors = models.ManyToManyField(OrderItemProductFlavor)
    juices = models.ManyToManyField(OrderItemProductJuice)
    teas = models.ManyToManyField(OrderItemProductTea)

    def calculate_item_total(self):
        item_total = self.price * self.quantity
        for order_item_product_flavor in self.orderitem_set.all():
            item_total += order_item_product_flavor.price
        return item_total

    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
        self.total = self.calculate_item_total()
        super().save(*args, **kwargs)


class Order(models.Model):
    customer_name = models.CharField(max_length=200)
    special_instructions = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    total = models.DecimalField(default=0, max_digits=4, decimal_places=2)

    def calulate_order_total(self):
        total = Decimal(0)
        for order_item in self.orderitem_set.all():
            total += order_item.calculate_item_total()
        return total

    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
        self.total = self.calculate_order_total()
        super().save(*args, **kwargs)
