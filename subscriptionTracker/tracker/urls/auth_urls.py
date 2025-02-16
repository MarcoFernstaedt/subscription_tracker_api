from django.urls import path
from Tracker.views.auth_views import SignUpView, LogoutView
from rest_framework.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", LogoutView.as_view(), name="logout"),
]