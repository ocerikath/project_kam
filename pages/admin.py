from django.contrib import admin
from .models import Category, Product, Lead


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price")
    list_filter = ("category",)
    search_fields = ("name", "description")

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone", "email", "product_name", "comment", "created_at")
    list_filter = ("created_at",)
    search_fields = ("full_name", "phone", "email", "product_name", "comment")
    readonly_fields = ("created_at",)