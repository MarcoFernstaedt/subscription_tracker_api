from django.urls import path, include

urlpatterns = [
    path("auth/", include("tracker.urls.auth_urls")),
    path("users/", include("tracker.urls.user_urls")),
    path("subscriptions/", include("tracker.urls.subscription_urls")),
]
