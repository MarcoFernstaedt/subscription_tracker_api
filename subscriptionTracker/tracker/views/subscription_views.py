from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.utils.timezone import now
from rest_framework.response import Response
from rest_framework import status
from Tracker.models import Subscription
from Tracker.serializers.subscription_serializers import SubscriptionSerializer

class SubscriptionViewSet(ModelViewSet):
    """Handles CRUD operations for subscriptions"""
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def get_permissions(self):
        """Different permissions for different actions"""
        if self.action in ["destroy", "list"]:  
            self.permission_classes = [IsAdminUser]  # Only admins can delete & list all subscriptions
        else:
            self.permission_classes = [IsAuthenticated]  # Authenticated users can manage their subscriptions
        return super().get_permissions()

    def list(self, request):
        """Admin can view all subscriptions"""
        if request.user.is_staff:  
            return super().list(request)
        return Response({"detail": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, pk=None):
        """Get a single subscription (only if it belongs to the user)"""
        subscription = self.get_object()
        if request.user == subscription.user or request.user.is_staff:
            serializer = self.get_serializer(subscription)
            return Response(serializer.data)
        return Response({"detail": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)

    def create(self, request):
        """Users can create their own subscriptions"""
        data = request.data.copy()  
        data["user"] = request.user.id  # Assign logged-in user automatically
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """Users can update only their own subscriptions"""
        subscription = self.get_object()
        if request.user == subscription.user or request.user.is_staff:
            return super().update(request, pk)
        return Response({"detail": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        """Only Admins can delete subscriptions"""
        return super().destroy(request, pk)

    def get_upcoming_renewals(self, request):
        """Get all subscriptions that are renewing within the next 30 days"""
        upcoming_subs = Subscription.objects.filter(
            renewal_date__range=[now().date(), now().date() + timedelta(days=30)]
        )
        serializer = self.get_serializer(upcoming_subs, many=True)
        return Response(serializer.data)
