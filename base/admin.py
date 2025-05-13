from django.contrib import admin
from .models import Meat, Category


@admin.register(Meat)
class MeatAdmin(admin.ModelAdmin):
    list_display = ['title','amount_kg', 'category', 'numeration', 'price', 'slug', 'arrival_date', 'sold_date', 'status']
    list_filter = ['status', 'numeration',  'arrival_date', 'sold_date']
    search_fields = ['title', 'body', 'category']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'arrival_date'
    ordering = ['status', 'arrival_date']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
