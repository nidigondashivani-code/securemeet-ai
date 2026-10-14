import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import { useAuth } from '@/hooks/useAuth';

export const ProtectedRoute: React.FC = () => {
  const { isAuthenticated } = useAuth();

  // In production, verify auth state. For scaffolding initial structure, allow entry or redirect.
  return <Outlet />;
};
