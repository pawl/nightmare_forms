from django.contrib import admin

from . import models


class EspressoShotAdmin(admin.ModelAdmin):
    pass


class FlavorCategoryAdmin(admin.ModelAdmin):
    pass


class FlavorAdmin(admin.ModelAdmin):
    pass


class JuiceAdmin(admin.ModelAdmin):
    pass


class MilkAdmin(admin.ModelAdmin):
    pass


class RoomChoiceAdmin(admin.ModelAdmin):
    pass


class IceChoiceAdmin(admin.ModelAdmin):
    pass


class AllowedMilksInline(admin.StackedInline):
    model = models.Product.allowed_milks.through
    extra = 0


class AllowedSizesInline(admin.StackedInline):
    model = models.Product.allowed_sizes.through
    extra = 0


class AllowedFlavorsInline(admin.StackedInline):
    model = models.Product.allowed_flavors.through
    extra = 0


class AllowedSweetenersInline(admin.StackedInline):
    model = models.Product.allowed_sweeteners.through
    extra = 0


class AllowedEspressoShotsInline(admin.StackedInline):
    model = models.Product.allowed_espresso_shots.through
    extra = 0


class AllowedJuicesInline(admin.StackedInline):
    model = models.Product.allowed_juices.through
    extra = 0


class AllowedToppingsInline(admin.StackedInline):
    model = models.Product.allowed_toppings.through
    extra = 0


class AllowedTeasInline(admin.StackedInline):
    model = models.Product.allowed_teas.through
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        AllowedMilksInline,
        AllowedSizesInline,
        AllowedFlavorsInline,
        AllowedSweetenersInline,
        AllowedEspressoShotsInline,
        AllowedJuicesInline,
        AllowedToppingsInline,
        AllowedTeasInline,
    ]


class SizeAdmin(admin.ModelAdmin):
    pass


class SweetenerAdmin(admin.ModelAdmin):
    pass


class TeaAdmin(admin.ModelAdmin):
    pass


class ToppingCategoryAdmin(admin.ModelAdmin):
    pass


class ToppingAdmin(admin.ModelAdmin):
    pass


class CustomizedProductFlavorsInline(admin.StackedInline):
    model = models.CustomizedProduct.flavors.through
    extra = 0


class CustomizedProductSweetenersInline(admin.StackedInline):
    model = models.CustomizedProduct.sweeteners.through
    extra = 0


class CustomizedProductEspressoShotsInline(admin.StackedInline):
    model = models.CustomizedProduct.espresso_shots.through
    extra = 0


class CustomizedProductJuicesInline(admin.StackedInline):
    model = models.CustomizedProduct.juices.through
    extra = 0


class CustomizedProductToppingsInline(admin.StackedInline):
    model = models.CustomizedProduct.toppings.through
    extra = 0


class CustomizedProductTeasInline(admin.StackedInline):
    model = models.CustomizedProduct.teas.through
    extra = 0


class CustomizedProductAdmin(admin.ModelAdmin):
    inlines = [
        CustomizedProductFlavorsInline,
        CustomizedProductSweetenersInline,
        CustomizedProductEspressoShotsInline,
        CustomizedProductJuicesInline,
        CustomizedProductToppingsInline,
        CustomizedProductTeasInline,
    ]


admin.site.register(models.Juice, JuiceAdmin)
admin.site.register(models.EspressoShot, EspressoShotAdmin)
admin.site.register(models.FlavorCategory, FlavorCategoryAdmin)
admin.site.register(models.Flavor, FlavorAdmin)
admin.site.register(models.Milk, MilkAdmin)
admin.site.register(models.RoomChoice, RoomChoiceAdmin)
admin.site.register(models.IceChoice, IceChoiceAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Size, SizeAdmin)
admin.site.register(models.Sweetener, SweetenerAdmin)
admin.site.register(models.Tea, TeaAdmin)
admin.site.register(models.ToppingCategory, ToppingCategoryAdmin)
admin.site.register(models.Topping, ToppingAdmin)
admin.site.register(models.CustomizedProduct, CustomizedProductAdmin)
