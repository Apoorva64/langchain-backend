from django.db import models
from jsonschema import validate, exceptions
from django.core.exceptions import ValidationError
from langchain.llms import get_type_to_cls_dict


# Create your models here.

class NodeType(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    json_schema = models.JSONField()

    def __str__(self):
        return self.category + ' - ' + self.name


class EdgeType(models.Model):
    node_a = models.ForeignKey(NodeType, on_delete=models.CASCADE, related_name='node_a')
    node_b = models.ForeignKey(NodeType, on_delete=models.CASCADE, related_name='node_b')

    def __str__(self):
        return f'{self.node_a} -> {self.node_b}'


class Node(models.Model):
    node_type = models.ForeignKey(NodeType, on_delete=models.CASCADE)
    data = models.JSONField()

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)
        # validate data against json schema
        if self.data:
            try:
                validate(self.data, self.node_type.json_schema)
            except exceptions.ValidationError as e:
                raise ValidationError(
                    {'data': f'Invalid data: {e.message}'}
                )

    def __str__(self):
        return "Node: " + str(self.node_type)

    def create_node(self):
        if self.node_type.category == "LLM":
            node = get_type_to_cls_dict()[self.node_type.name]()(**self.data)
            return node
        raise ValueError("Node type not supported")


class Edge(models.Model):
    edge_type = models.ForeignKey(EdgeType, on_delete=models.CASCADE)
    node_a = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='node_a')
    node_b = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='node_b')

    def __str__(self):
        return f'{self.node_a} -> {self.node_b}'


class Chain(models.Model):
    name = models.CharField(max_length=100)
    nodes = models.ManyToManyField(Node, through='ChainNode')

    def __str__(self):
        return self.name

    def create_chain(self):
        # use | to concatenate the nodes
        chain = self.nodes.first().create_node()
        for chain_node in self.nodes.all()[1:]:
            chain |= chain_node.create_node()
        return chain


class ChainNode(models.Model):
    chain = models.ForeignKey(Chain, on_delete=models.CASCADE)
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    order = models.IntegerField()

    def __str__(self):
        return f'{self.chain} - {self.node} - {self.order}'
