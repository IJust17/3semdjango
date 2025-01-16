from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Author, File, Comment

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

    # (1) Имя автора не должно быть только из цифр
    def validate_name(self, value):
        if value.isdigit():
            raise ValidationError("Имя автора не может состоять только из цифр.")
        return value


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

    # (2) Имя файла >= 3 символов
    def validate_name(self, value):
        if len(value) < 3:
            raise ValidationError("Имя файла должно содержать минимум 3 символа.")
        return value


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    # (3) Не содержит forbidden
    def validate_text(self, value):
        if "forbidden" in value.lower():
            raise ValidationError("Комментарий не должен содержать слово 'forbidden'.")
        return value
