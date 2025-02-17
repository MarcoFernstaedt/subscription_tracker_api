from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tracker.views.user_views import UserViewSet

router = DefaultRouter()
router.register(r"", UserViewSet)

urlpatterns = router.urls
