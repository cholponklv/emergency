# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet,TargetViewSet

router = DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'targets', TargetViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
