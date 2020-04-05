from coffee import models
from django.contrib import admin


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


class ProductAdmin(admin.ModelAdmin):
    pass


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


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Juice, JuiceAdmin)
admin.site.register(models.EspressoShot, EspressoShotAdmin)
admin.site.register(models.FlavorCategory, FlavorCategoryAdmin)
admin.site.register(models.Flavor, FlavorAdmin)
admin.site.register(models.Milk, MilkAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Size, SizeAdmin)
admin.site.register(models.Sweetener, SweetenerAdmin)
admin.site.register(models.Tea, TeaAdmin)
admin.site.register(models.ToppingCategory, ToppingCategoryAdmin)
admin.site.register(models.Topping, ToppingAdmin)
admin.site.register(models.Order, OrderAdmin)
