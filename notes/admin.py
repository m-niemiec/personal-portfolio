from django.contrib import admin
from .models import Note, Category, SubCategory


admin.site.register(Note)
admin.site.register(Category)
admin.site.register(SubCategory)
