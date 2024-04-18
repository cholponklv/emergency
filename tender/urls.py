# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TenderViewSet, TenderResultListView,DocumentTenderViewSet,AllDocumentsTendersView,DocumentResultTenderViewSet,AllDocumentsResultTendersView

router = DefaultRouter()
router.register(r'tenders', TenderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tenders/<int:tender_id>/documents/', DocumentTenderViewSet.as_view({'get': 'list', 'post': 'create'}), name='document-list'),
    path('tenders/<int:tender_id>/documents/<int:pk>/', DocumentTenderViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='document-detail'),
    path('tenders/<int:id>/results/', TenderResultListView.as_view(), name='tender-results-list'),
    path('tenders_documents/', AllDocumentsTendersView.as_view(), name='all-documents'),
    path('results/<int:result_id>/documents/', DocumentResultTenderViewSet.as_view({'get': 'list', 'post': 'create'}), name='document-list'),
    path('results/<int:result_id>/documents/<int:pk>/', DocumentResultTenderViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='document-detail'),
    path('results_documents/', AllDocumentsResultTendersView.as_view(), name='all-documents'),]
