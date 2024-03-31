# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TenderViewSet, TenderResultListView

router = DefaultRouter()
router.register(r'tenders', TenderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tenders/<int:id>/results/', TenderResultListView.as_view(), name='tender-results-list'),
    
]
