from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet, GaleryViewSet

router = DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'galery', GaleryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]