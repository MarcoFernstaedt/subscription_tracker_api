from rest_framework import serializers
from tracker.models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"  # Includes all model fields

    def validate(self, data):
        """Ensure renewal_date is in the future"""
        if data.get("renewal_date") and data["renewal_date"] < data["created_at"].date():
            raise serializers.ValidationError({"renewal_date": "Renewal date must be in the future."})
        return data
