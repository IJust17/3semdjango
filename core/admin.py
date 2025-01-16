from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats

from .models import Author, File, Comment
from .resources import FileResource



# 1) AuthorAdmin

@admin.register(Author)
class AuthorAdmin(SimpleHistoryAdmin):
    """
    Используем SimpleHistoryAdmin, чтобы в админке
    отображалась вкладка "History" для Author.
    """
    list_display = ('id', 'name')
    search_fields = ('name',)
    fieldsets = (
        ('Основное', {
            'fields': ('name',),
        }),
    )



# 2) FileAdmin

class FileAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    """
    Совмещаем импорт/экспорт (ImportExportModelAdmin)
    и историю изменений (SimpleHistoryAdmin).
    """
    resource_class = FileResource  # Для экспорта
    list_display = ('id', 'name', 'author_link', 'short_desc', 'created_at')
    list_filter = ('author', 'created_at')
    search_fields = ('name', 'description')

    fieldsets = (
        ('File Info', {
            'fields': ('author', 'name', 'file'),
        }),
        ('Extra', {
            'fields': ('description', 'created_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at',)

    def author_link(self, obj):
        return obj.author.name if obj.author else '-'
    author_link.short_description = 'Author'

    def short_desc(self, obj):
        return (obj.description[:30] + '...') if obj.description else '-'
    short_desc.short_description = 'Short desc'

    # форматы экспорта
    def get_export_formats(self):
        formats = [
            base_formats.CSV,    
            base_formats.XLSX,   
            base_formats.JSON,
            
        ]
        return [f for f in formats if f().can_export()]


admin.site.register(File, FileAdmin)



# 3) CommentAdmin

@admin.register(Comment)
class CommentAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'file', 'text', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('text', 'file__name')
    fields = ('file', 'text', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
