from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VacancyViewSet

router = DefaultRouter()
router.register(r'vacancy', VacancyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]