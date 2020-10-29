from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']

class PostSerializer(serializers.ModelSerializer):
    #author = AuthorSerializer()
    # username = serializers.ReadOnlyField(source='author.username')
    author_name = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = [
            'pk',
            #'author',
            # 'username',
            #'author_email',
            'author_name',
            'message',
            'created_at',
            'updated_at',
            'is_public',
        ]
