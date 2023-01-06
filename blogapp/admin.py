from django.contrib import admin
from .models import Blog

# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display =['title', 'date_added', 'last_modified']

    class Media(admin.ModelAdmin):
        js = ('tiny.js',)
