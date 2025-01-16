from import_export import resources
from .models import File

class FileResource(resources.ModelResource):
    """
    Настройка для экспорта File.
    """
    # экспорти только файлов у которых есть description
    def get_export_queryset(self, request):
        return self._meta.model.objects.exclude(description__exact='')

    # вывод поля name
    def dehydrate_name(self, file_obj):
        return f"[Exported] {file_obj.name}"

    # author_name
    def get_author_name(self, file_obj):
        return file_obj.author.name if file_obj.author else ''

    class Meta:
        model = File
        fields = ('id', 'name', 'author_name', 'description', 'created_at')
        export_order = ('id', 'author_name', 'name', 'description', 'created_at')
