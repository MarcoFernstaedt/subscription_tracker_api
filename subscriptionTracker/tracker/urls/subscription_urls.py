from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Tracker.views.subscription_views import SubscriptionViewSet

router = DefaultRouter()
router.register(r"", SubscriptionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("upcoming-renewals/", SubscriptionViewSet.as_view({"get": "get_upcoming_renewals"}), name="upcoming-renewals"),
]
