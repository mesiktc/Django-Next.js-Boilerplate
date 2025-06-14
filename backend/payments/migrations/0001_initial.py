from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(default='usd', max_length=3)),
                ('interval', models.CharField(default='month', max_length=20)),
                ('provider', models.CharField(choices=[('stripe', 'Stripe'), ('lemonsqueezy', 'LemonSqueezy')], max_length=20)),
                ('provider_price_id', models.CharField(max_length=255)),
                ('features', models.JSONField(default=list)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['price'],
            },
        ),
    ] 