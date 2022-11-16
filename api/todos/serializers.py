from rest_framework import serializers
from .models import Todo, Category
from pprint import pprint as p


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class TodoSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Todo
        fields = "__all__"

    def create(self, validated_data):
        category = validated_data.pop('category')
        obj, created = Category.objects.get_or_create(name=category['name'])
        p(obj)
        p(created)
        todo = Todo.objects.create(**validated_data, category=obj)
        return todo