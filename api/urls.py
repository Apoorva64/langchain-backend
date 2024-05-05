from django.urls import include, path
from rest_framework import routers
from .views import NodeTypeViewSet, EdgeTypeViewSet, NodeViewSet, EdgeViewSet

router = routers.DefaultRouter()

router.register(r'nodetypes', NodeTypeViewSet)
router.register(r'edgetypes', EdgeTypeViewSet)
router.register(r'nodes', NodeViewSet)
router.register(r'edges', EdgeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
