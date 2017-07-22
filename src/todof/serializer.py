# coding=utf-8
from rest_framework import serializers
from todof.models import TodoItem


class TodoItemSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.ReadOnlyField()

    class Meta:
        model = TodoItem
        fields = ('url', 'title', 'completed', 'order')
