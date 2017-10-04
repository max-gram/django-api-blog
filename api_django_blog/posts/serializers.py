from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'seo_keywords', 'seo_description', 'pub_date')
        # read_only_fields = ('title', 'slug', 'seo_keywords', 'seo_description', 'pub_date')