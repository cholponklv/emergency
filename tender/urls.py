# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TenderViewSet

router = DefaultRouter()
router.register(r'tenders', TenderViewSet)

urlpatterns = [
    path('', include(router.urls)),
     path('tenders/<int:pk>/results/create/', TenderViewSet.as_view({'post': 'create_result'}), name='create-tender-result'),
]
