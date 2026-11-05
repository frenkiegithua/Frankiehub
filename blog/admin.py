from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created', 'updated')
    list_filter = ('status', 'created')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
