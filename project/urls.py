from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, PhotoViewSet, DocumentViewSet,AllPhotosView, AllDocumentsView

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

# Добавляем URL-шаблоны для CRUD операций документов, учитывая идентификатор проекта
urlpatterns = [
    path('projects/<int:project_id>/photos/', PhotoViewSet.as_view({'get': 'list', 'post': 'create'}), name='photo-list'),
    path('projects/<int:project_id>/photos/<int:pk>/', PhotoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='photo-detail'),
    path('projects/<int:project_id>/documents/', DocumentViewSet.as_view({'get': 'list', 'post': 'create'}), name='document-list'),
    path('projects/<int:project_id>/documents/<int:pk>/', DocumentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='document-detail'),
    path('photos/', AllPhotosView.as_view(), name='all-photos'),
    path('documents/', AllDocumentsView.as_view(), name='all-documents'),
]

urlpatterns += router.urls
