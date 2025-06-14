from django.db import migrations

def add_initial_plans(apps, schema_editor):
    PaymentPlan = apps.get_model('payments', 'PaymentPlan')
    
    plans = [
        {
            'name': 'Basic',
            'description': 'Perfect for individuals and small projects',
            'price': 9.99,
            'currency': 'usd',
            'interval': 'month',
            'provider': 'stripe',
            'provider_price_id': 'price_basic',
            'features': [
                'Basic feature 1',
                'Basic feature 2',
                'Basic feature 3'
            ],
            'is_active': True
        },
        {
            'name': 'Pro',
            'description': 'Ideal for growing businesses',
            'price': 19.99,
            'currency': 'usd',
            'interval': 'month',
            'provider': 'stripe',
            'provider_price_id': 'price_pro',
            'features': [
                'All Basic features',
                'Pro feature 1',
                'Pro feature 2',
                'Priority support'
            ],
            'is_active': True
        },
        {
            'name': 'Enterprise',
            'description': 'For large organizations with advanced needs',
            'price': 49.99,
            'currency': 'usd',
            'interval': 'month',
            'provider': 'stripe',
            'provider_price_id': 'price_enterprise',
            'features': [
                'All Pro features',
                'Enterprise feature 1',
                'Enterprise feature 2',
                '24/7 dedicated support',
                'Custom integrations'
            ],
            'is_active': True
        }
    ]
    
    for plan_data in plans:
        PaymentPlan.objects.create(**plan_data)

def remove_initial_plans(apps, schema_editor):
    PaymentPlan = apps.get_model('payments', 'PaymentPlan')
    PaymentPlan.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_plans, remove_initial_plans),
    ] 