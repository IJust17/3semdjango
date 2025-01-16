import django_filters
from django_filters import rest_framework as filters
from .models import File

class FileFilter(filters.FilterSet):
    name_exact = filters.CharFilter(field_name='name', lookup_expr='exact')
    name_icontains = filters.CharFilter(field_name='name', lookup_expr='icontains')
    author_name = filters.CharFilter(field_name='author__name', lookup_expr='icontains')
    created_before = filters.DateFilter(field_name='created_at', lookup_expr='lte')
    created_after = filters.DateFilter(field_name='created_at', lookup_expr='gte')

    class Meta:
        model = File
        fields = [
            'name_exact',
            'name_icontains',
            'author_name',
            'created_before',
            'created_after',
        ]
