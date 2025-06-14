from rest_framework import serializers
from .models import Subscription, Payment, PaymentPlan

class PaymentPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentPlan
        fields = ['id', 'name', 'description', 'price', 'currency', 
                 'interval', 'provider', 'provider_price_id', 'features']
        read_only_fields = ['id']

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'provider', 'status', 'current_period_start', 
                 'current_period_end', 'cancel_at_period_end', 'created_at']
        read_only_fields = ['id', 'created_at']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'provider', 'status', 'amount', 'currency', 
                 'created_at']
        read_only_fields = ['id', 'created_at']

class CreateCheckoutSessionSerializer(serializers.Serializer):
    price_id = serializers.CharField()
    success_url = serializers.URLField()
    cancel_url = serializers.URLField() 