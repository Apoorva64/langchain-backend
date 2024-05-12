from rest_framework import viewsets
from .models import NodeType, EdgeType, Node, Edge, Chain
from .serializers import NodeTypeSerializer, EdgeTypeSerializer, NodeSerializer, EdgeSerializer, ChainSerializer

from rest_framework.views import APIView
from django.http import StreamingHttpResponse


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


class ChainViewSet(viewsets.ModelViewSet):
    queryset = Chain.objects.all()
    serializer_class = ChainSerializer


class ChainInvokeAPIView(APIView):

    def post(self, request, format=None):
        chain = Chain.objects.get(id=request.data['chain_id'])
        instance = chain.create_chain()
        response = instance.stream(**request.data['params'])

        def iterate_response():
            for i in response:
                yield i

        return StreamingHttpResponse(iterate_response())
