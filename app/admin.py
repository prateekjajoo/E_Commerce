from django.contrib import admin
from .models import Product, ProductImage, BestOffer
from admin_auto_filters.filters import AutocompleteFilter

# Register your models here.


class ProductFilter(AutocompleteFilter):
    title = "Product"
    field_name = 'product_id'


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    max_num = 10
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'company_name', 'model_name', 'prize', )
    list_filter = ('category', 'company_name', )
    search_fields = ['model_name']
    inlines = [ProductImageInline, ]


class BestOfferAdmin(admin.ModelAdmin):
    exclude = ("seller_id",)
    autocomplete_fields = ['product_id']
    list_filter = [ProductFilter]
    list_display = ['seller_id', 'product_id', 'best_prize']

    class Media:
        pass

    def save_model(self, request, obj, form, change):
        obj.seller_id = request.user
        super(self.__class__, self).save_model(request, obj, form, change)


admin.site.register(Product, ProductAdmin)
admin.site.register(BestOffer, BestOfferAdmin)
