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
        cat_instance = Category.objects.get(name=category['name'])
        todo = Todo.objects.create(**validated_data, category=cat_instance)
        return todo