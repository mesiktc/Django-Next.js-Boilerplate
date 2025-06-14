from django.db import models
from django.conf import settings

class PaymentPlan(models.Model):
    PAYMENT_PROVIDER_CHOICES = [
        ('stripe', 'Stripe'),
        ('lemonsqueezy', 'LemonSqueezy'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='usd')
    interval = models.CharField(max_length=20, default='month')  # month, year
    provider = models.CharField(max_length=20, choices=PAYMENT_PROVIDER_CHOICES)
    provider_price_id = models.CharField(max_length=255)  # Stripe price ID or LemonSqueezy variant ID
    features = models.JSONField(default=list)  # List of features included in the plan
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['price']

    def __str__(self):
        return f"{self.name} - {self.price} {self.currency}/{self.interval}"

class Subscription(models.Model):
    PAYMENT_PROVIDER_CHOICES = [
        ('stripe', 'Stripe'),
        ('lemonsqueezy', 'LemonSqueezy'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('canceled', 'Canceled'),
        ('expired', 'Expired'),
        ('trial', 'Trial'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    provider = models.CharField(max_length=20, choices=PAYMENT_PROVIDER_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='trial')
    provider_subscription_id = models.CharField(max_length=255)
    current_period_start = models.DateTimeField()
    current_period_end = models.DateTimeField()
    cancel_at_period_end = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'provider')

    def __str__(self):
        return f"{self.user.email} - {self.provider} - {self.status}"

class Payment(models.Model):
    PAYMENT_PROVIDER_CHOICES = [
        ('stripe', 'Stripe'),
        ('lemonsqueezy', 'LemonSqueezy'),
    ]

    STATUS_CHOICES = [
        ('succeeded', 'Succeeded'),
        ('pending', 'Pending'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    provider = models.CharField(max_length=20, choices=PAYMENT_PROVIDER_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='usd')
    provider_payment_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} - {self.provider} - {self.amount} {self.currency}" 