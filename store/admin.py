from django.contrib import admin
from .models import Product, Variation

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'created_at', 'updated_at', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}	# slug field will be automatically populated with product_name

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_activate')
    list_editable = ('is_activate',)
    list_filter = ('product', 'variation_category','variation_value' ,'is_activate')

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)