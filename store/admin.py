from django.contrib import admin


from store import models


class SizeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name"
    ]

    list_display_links = [
        "id",
        "name"
    ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "created_at",
        "updated_at"
    ]

    list_display_links = [
        "id", 
        "name"
    ]

    prepopulated_fields = {
        "slug": ["name"]
    }


class ProductAdmin(admin.ModelAdmin):
    fields = [
        "category",
        "title",
        "brand",
        "description",
        # "available_sizes",
        "size",
        "slug",
        "price",
        "image",
        "get_image_tag",
        "featured",
        "published"

    ]
    list_display = [
        "id",
        "get_image_tag",
        "title",
        "category",
        # "available_sizes_str",
        "size",
        "price",
        "featured",
        "published",
        "created_at",
        "updated_at"
    ]

    list_display_links = [
        "id",
        "get_image_tag", 
        "title"
    ]

    list_editable = [
        "published",
        "featured"
    ]

    prepopulated_fields = {
        "slug": ["title"]
    }

    readonly_fields = [
        "get_image_tag"
    ]


    list_filter = [
        "category",
        "size",
        "created_at",
        "updated_at",
        "featured",
        "published"
    ]

    search_fields = [
        "title",
        "description",

    ]



admin.site.register(models.Size, SizeAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
