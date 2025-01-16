from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, FileViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'files', FileViewSet, basename='file')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]
