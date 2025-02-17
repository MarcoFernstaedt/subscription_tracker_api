from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from tracker.serializers.auth_serializers import SignUpSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

User = get_user_model()

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer

    def get_permissions(self):
        if self.action in ["list", "destroy"]:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
