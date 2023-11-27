from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, MemberTeamViewSet, ProjectViewSet,PhotoViewSet

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'membersteam', MemberTeamViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'photo', PhotoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]