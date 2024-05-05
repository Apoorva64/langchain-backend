from rest_framework import serializers
from .models import NodeType, EdgeType, Node, Edge


class NodeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NodeType
        fields = '__all__'


class EdgeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EdgeType
        fields = '__all__'


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = '__all__'


class EdgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edge
        fields = '__all__'


