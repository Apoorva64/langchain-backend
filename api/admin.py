# Register your models here.
from django.contrib import admin
from .models import NodeType, EdgeType, Node, Edge

admin.site.register(NodeType)
admin.site.register(EdgeType)
admin.site.register(Node)
admin.site.register(Edge)
