from django.contrib import admin
from .models import Category, Blog

# class CategoryAdmin(admin.ModelAdmin):
#     pass


admin.site.register(Category)
admin.site.register(Blog)
