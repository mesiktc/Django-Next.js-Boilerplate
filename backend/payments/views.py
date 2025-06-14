from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Subscription, Payment, PaymentPlan
from .serializers import (
    SubscriptionSerializer, PaymentSerializer, CreateCheckoutSessionSerializer,
    PaymentPlanSerializer
)
import stripe
from datetime import datetime, timezone
import requests

class PaymentPlanViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]  # Allow anyone to view plans
    serializer_class = PaymentPlanSerializer
    queryset = PaymentPlan.objects.filter(is_active=True)

class SubscriptionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)

    @action(detail=False, methods=['post'])
    def create_checkout_session(self, request):
        serializer = CreateCheckoutSessionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        if settings.PAYMENT_PROVIDER == 'stripe':
            return self._create_stripe_checkout_session(serializer.validated_data)
        elif settings.PAYMENT_PROVIDER == 'lemonsqueezy':
            return self._create_lemonsqueezy_checkout_session(serializer.validated_data)
        else:
            return Response(
                {'error': 'Invalid payment provider'},
                status=status.HTTP_400_BAD_REQUEST
            )

    def _create_stripe_checkout_session(self, data):
        try:
            stripe.api_key = settings.STRIPE_SECRET_KEY
            
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price': data['price_id'],
                    'quantity': 1,
                }],
                mode='subscription',
                success_url=data['success_url'],
                cancel_url=data['cancel_url'],
                customer_email=request.user.email,
                metadata={
                    'user_id': request.user.id
                }
            )
            
            return Response({'session_id': checkout_session.id})
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    def _create_lemonsqueezy_checkout_session(self, data):
        try:
            headers = {
                'Authorization': f'Bearer {settings.LEMON_SQUEEZY_API_KEY}',
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
            
            response = requests.post(
                'https://api.lemonsqueezy.com/v1/checkouts',
                headers=headers,
                json={
                    'data': {
                        'type': 'checkouts',
                        'attributes': {
                            'product_id': data['price_id'],
                            'checkout_data': {
                                'email': request.user.email,
                                'custom': {
                                    'user_id': request.user.id
                                }
                            },
                            'success_url': data['success_url'],
                            'cancel_url': data['cancel_url']
                        }
                    }
                }
            )
            
            if response.status_code == 201:
                return Response(response.json())
            else:
                return Response(
                    {'error': response.text},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class PaymentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user) 