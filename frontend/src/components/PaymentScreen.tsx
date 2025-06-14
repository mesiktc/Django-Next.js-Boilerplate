import React from 'react';
import { usePayment } from '../contexts/PaymentContext';
import { Card, Button, Spinner, Alert } from 'react-bootstrap';

const PaymentScreen: React.FC = () => {
  const { subscription, plans, loading, error, createCheckoutSession } = usePayment();

  if (loading) {
    return (
      <div className="d-flex justify-content-center align-items-center" style={{ minHeight: '400px' }}>
        <Spinner animation="border" role="status">
          <span className="visually-hidden">Loading...</span>
        </Spinner>
      </div>
    );
  }

  if (error) {
    return (
      <Alert variant="danger" className="m-3">
        {error}
      </Alert>
    );
  }

  if (subscription) {
    return (
      <Alert variant="success" className="m-3">
        You are currently subscribed to the {subscription.provider} plan.
        Your subscription will renew on {new Date(subscription.current_period_end).toLocaleDateString()}.
      </Alert>
    );
  }

  return (
    <div className="container py-5">
      <h2 className="text-center mb-5">Choose Your Plan</h2>
      <div className="row row-cols-1 row-cols-md-3 g-4">
        {plans.map((plan) => (
          <div key={plan.id} className="col">
            <Card className="h-100">
              <Card.Body>
                <Card.Title className="text-center">{plan.name}</Card.Title>
                <Card.Subtitle className="mb-2 text-muted text-center">
                  {plan.price} {plan.currency}/{plan.interval}
                </Card.Subtitle>
                {plan.description && (
                  <Card.Text className="text-center mb-3">
                    {plan.description}
                  </Card.Text>
                )}
                <ul className="list-unstyled mt-3 mb-4">
                  {plan.features.map((feature, index) => (
                    <li key={index} className="mb-2">
                      ✓ {feature}
                    </li>
                  ))}
                </ul>
                <div className="d-grid">
                  <Button
                    variant="primary"
                    onClick={() => createCheckoutSession(plan.provider_price_id)}
                  >
                    Subscribe Now
                  </Button>
                </div>
              </Card.Body>
            </Card>
          </div>
        ))}
      </div>
    </div>
  );
};

export default PaymentScreen; 