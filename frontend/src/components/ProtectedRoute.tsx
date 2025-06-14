import React from 'react';
import { Navigate } from 'react-router-dom';
import { usePayment } from '../contexts/PaymentContext';
import { Spinner } from 'react-bootstrap';

interface ProtectedRouteProps {
  children: React.ReactNode;
}

const ProtectedRoute: React.FC<ProtectedRouteProps> = ({ children }) => {
  const { subscription, loading } = usePayment();

  if (loading) {
    return (
      <div className="d-flex justify-content-center align-items-center" style={{ minHeight: '400px' }}>
        <Spinner animation="border" role="status">
          <span className="visually-hidden">Loading...</span>
        </Spinner>
      </div>
    );
  }

  if (!subscription) {
    return <Navigate to="/payment" replace />;
  }

  return <>{children}</>;
};

export default ProtectedRoute; 