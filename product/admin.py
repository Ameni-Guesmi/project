from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin
from product.models import category, product, Images

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id_category', 'type_category']
    list_filter = ['type_category']
    
class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "type_category"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = category.objects.add_related_count(
                qs,
                product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = category.objects.add_related_count(qs,
                 product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'
    

    
class productImageInline(admin.TabularInline):
    model = Images
    extra = 5
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['nom', 'category','description', 'prix', 'stock', 'image_tag']
    list_filter = ['category']
    readonly_fields = ('image_tag',)
    inlines = [productImageInline]

admin.site.register(category,CategoryAdmin2)
admin.site.register(product, ProductAdmin)
admin.site.register(Images)