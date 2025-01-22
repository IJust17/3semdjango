from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Author, File, Comment
from .serializers import AuthorSerializer, FileSerializer, CommentSerializer
from .filters import FileFilter


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # @action(methods=['GET'], detail=False)

    @action(methods=['GET'], detail=False)
    def bi_or_abc(self, request):
        """
        авторов, в имени которых есть 'bi' или 'abc',
        при этом они не начинаются на 'me'.
        """
        # минимум два запроса с Q включающие AND NOT
        qs = self.get_queryset().filter(
            (Q(name__icontains='bi') | Q(name__icontains='abc'))
            & ~Q(name__startswith='me')
        )
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    filterset_class = FileFilter
    search_fields = ['name', 'description']  # для SearchFilter из DRF

    @action(methods=['GET'], detail=False)
    def cat_or_stalker(self, request):
        """
        файлы, у которых description содержит 'cat' или 'stalker',
        и исключит те, у которых name содержит 'bi'.
        """
        qs = self.get_queryset().filter(
            (Q(description__icontains='cat') | Q(description__icontains='stalker'))
            & ~Q(name__icontains='bi')
        )
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(methods=['POST'], detail=True)
    def change_description(self, request, pk=None):
        """
        изменение description файла POST-запросом:
        {
           
        }
        """
        file_obj = self.get_object()
        new_desc = request.data.get('description', '')
        file_obj.description = new_desc
        file_obj.save()
        return Response({
            'status': 'description updated',
            'file_id': file_obj.id,
            'new_description': new_desc
        })


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(methods=['GET'], detail=False)
    def django_comments(self, request):
        """
        выбрать все комментарии, содержащие 'django' в тексте.
        """
        qs = self.get_queryset().filter(text__icontains='django')
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
