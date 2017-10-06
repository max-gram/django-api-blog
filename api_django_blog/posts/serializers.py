from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    thumb = serializers.ImageField(read_only=True)
    
    class Meta:
        model = Post
        fields = ('title', 'slug', 'body', 'thumb', 'seo_keywords', 'seo_description', 'pub_date')
        read_only_fields = ('title', 'slug', 'body', 'seo_keywords', 'seo_description', 'pub_date')