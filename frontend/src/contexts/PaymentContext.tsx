import React, { createContext, useContext, useState, useEffect } from 'react';
import axios from 'axios';

interface PaymentPlan {
  id: number;
  name: string;
  description: string;
  price: number;
  currency: string;
  interval: string;
  provider: 'stripe' | 'lemonsqueezy';
  provider_price_id: string;
  features: string[];
}

interface PaymentContextType {
  subscription: any;
  plans: PaymentPlan[];
  loading: boolean;
  error: string | null;
  createCheckoutSession: (priceId: string) => Promise<void>;
}

const PaymentContext = createContext<PaymentContextType | undefined>(undefined);

export const PaymentProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [subscription, setSubscription] = useState<any>(null);
  const [plans, setPlans] = useState<PaymentPlan[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchSubscription();
    fetchPlans();
  }, []);

  const fetchSubscription = async () => {
    try {
      const response = await axios.get('/api/v1/payments/subscriptions/');
      setSubscription(response.data[0] || null);
    } catch (err) {
      setError('Failed to fetch subscription');
    } finally {
      setLoading(false);
    }
  };

  const fetchPlans = async () => {
    try {
      const response = await axios.get('/api/v1/payments/plans/');
      setPlans(response.data);
    } catch (err) {
      setError('Failed to fetch payment plans');
    }
  };

  const createCheckoutSession = async (priceId: string) => {
    try {
      setLoading(true);
      const response = await axios.post('/api/v1/payments/subscriptions/create_checkout_session/', {
        price_id: priceId,
        success_url: `${window.location.origin}/payment/success`,
        cancel_url: `${window.location.origin}/payment/cancel`,
      });

      if (response.data.session_id) {
        // Redirect to Stripe Checkout
        window.location.href = `https://checkout.stripe.com/pay/${response.data.session_id}`;
      } else if (response.data.data?.attributes?.url) {
        // Redirect to LemonSqueezy Checkout
        window.location.href = response.data.data.attributes.url;
      }
    } catch (err) {
      setError('Failed to create checkout session');
    } finally {
      setLoading(false);
    }
  };

  return (
    <PaymentContext.Provider
      value={{
        subscription,
        plans,
        loading,
        error,
        createCheckoutSession,
      }}
    >
      {children}
    </PaymentContext.Provider>
  );
};

export const usePayment = () => {
  const context = useContext(PaymentContext);
  if (context === undefined) {
    throw new Error('usePayment must be used within a PaymentProvider');
  }
  return context;
}; 