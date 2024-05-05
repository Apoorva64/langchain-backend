from rest_framework import viewsets
from .models import NodeType, EdgeType, Node, Edge
from .serializers import NodeTypeSerializer, EdgeTypeSerializer, NodeSerializer, EdgeSerializer


class NodeTypeViewSet(viewsets.ModelViewSet):
    queryset = NodeType.objects.all()
    serializer_class = NodeTypeSerializer


class EdgeTypeViewSet(viewsets.ModelViewSet):
    queryset = EdgeType.objects.all()
    serializer_class = EdgeTypeSerializer


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer


class EdgeViewSet(viewsets.ModelViewSet):
    queryset = Edge.objects.all()
    serializer_class = EdgeSerializer

