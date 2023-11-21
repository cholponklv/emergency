from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, MemberTeamViewSet, ProjectViewSet

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'membersteam', MemberTeamViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]