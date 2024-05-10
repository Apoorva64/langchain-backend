# Register your models here.
from django.contrib import admin
from django.db import models
from djangocodemirror.widgets import CodeMirrorWidget

from .models import NodeType, EdgeType, Node, Edge, Chain, ChainNode

admin.site.register(NodeType)
admin.site.register(EdgeType)
admin.site.register(Edge)


class NodeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': CodeMirrorWidget(config_name='javascript', embed_config=True)}

    }


admin.site.register(Node, NodeAdmin)


class ChainNodeInline(admin.TabularInline):
    model = ChainNode
    extra = 1


class ChainAdmin(admin.ModelAdmin):
    inlines = [ChainNodeInline]


admin.site.register(Chain, ChainAdmin)
