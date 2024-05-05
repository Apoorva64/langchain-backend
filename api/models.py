from django.db import models


# Create your models here.

class NodeType(models.Model):
    node_type = models.CharField(max_length=100)
    json_schema = models.JSONField()

    def __str__(self):
        return self.node_type


class EdgeType(models.Model):
    node_a = models.ForeignKey(NodeType, on_delete=models.CASCADE, related_name='node_a')
    node_b = models.ForeignKey(NodeType, on_delete=models.CASCADE, related_name='node_b')

    def __str__(self):
        return f'{self.node_a} -> {self.node_b}'


class Node(models.Model):
    node_type = models.ForeignKey(NodeType, on_delete=models.CASCADE)
    data = models.JSONField()

    def __str__(self):
        return self.node_type


class Edge(models.Model):
    edge_type = models.ForeignKey(EdgeType, on_delete=models.CASCADE)
    node_a = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='node_a')
    node_b = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='node_b')

    def __str__(self):
        return f'{self.node_a} -> {self.node_b}'






