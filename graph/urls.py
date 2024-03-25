from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Graph1ViewSet, Graph2ViewSet, Graph3ViewSet, Graph4ViewSet

router = DefaultRouter()
router.register(r'graph1', Graph1ViewSet)
router.register(r'graph2', Graph2ViewSet)
router.register(r'graph3', Graph3ViewSet)
router.register(r'graph4', Graph4ViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
