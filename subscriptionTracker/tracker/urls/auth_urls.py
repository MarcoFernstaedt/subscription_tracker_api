from django.urls import path
from tracker.views.auth_views import SignUpView, Loggout
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  # Ensure correct import

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", Loggout.as_view(), name="logout"),
]
