from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'date_of_publication', 'is_published')
    list_filter = ('date_of_publication',)
    search_fields = ('date_of_publication', 'is_published')
