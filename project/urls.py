from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, PhotoViewSet, DocumentViewSet,AllPhotosView, AllDocumentsView,SearchRUAPIView,SearchKGAPIView,SearchENAPIView

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('projects/<int:project_id>/photos/', PhotoViewSet.as_view({'get': 'list', 'post': 'create'}), name='photo-list'),
    path('projects/<int:project_id>/photos/<int:pk>/', PhotoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='photo-detail'),
    path('projects/<int:project_id>/documents/', DocumentViewSet.as_view({'get': 'list', 'post': 'create'}), name='document-list'),
    path('projects/<int:project_id>/documents/<int:pk>/', DocumentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='document-detail'),
    path('photos/', AllPhotosView.as_view(), name='all-photos'),
    path('documents/', AllDocumentsView.as_view(), name='all-documents'),
    path('api/search/ru/', SearchRUAPIView.as_view(), name='search_api_ru'),
    path('api/search/kg/', SearchKGAPIView.as_view(), name='search_api_kg'),
    path('api/search/en/', SearchENAPIView.as_view(), name='search_api_en'),
]

urlpatterns += router.urls
