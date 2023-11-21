from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TendersViewSet, TenderDocumentsViewSet

router = DefaultRouter()
router.register(r'tenders', TendersViewSet)
router.register(r'tenderdocuments', TenderDocumentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]