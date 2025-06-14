from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubscriptionViewSet, PaymentViewSet, PaymentPlanViewSet

router = DefaultRouter()
router.register(r'plans', PaymentPlanViewSet, basename='plan')
router.register(r'subscriptions', SubscriptionViewSet, basename='subscription')
router.register(r'payments', PaymentViewSet, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
] 