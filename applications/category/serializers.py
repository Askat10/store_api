from rest_framework import serializers
from applications.category.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['slug', 'title']
        read_only_fields = ['slug']