import React from 'react';
import { Link } from 'react-router-dom';

export const NotFoundPage: React.FC = () => {
  return (
    <div className="min-h-screen bg-slate-950 flex flex-col justify-center items-center text-center p-6">
      <h1 className="text-6xl font-extrabold text-emerald-500 mb-4">404</h1>
      <h2 className="text-2xl font-bold text-white mb-2">Resource Not Found</h2>
      <p className="text-slate-400 mb-6">The requested console page does not exist or has been relocated.</p>
      <Link
        to="/"
        className="px-5 py-2.5 bg-emerald-600 hover:bg-emerald-500 text-white rounded-lg text-sm font-semibold transition-colors"
      >
        Return to Dashboard
      </Link>
    </div>
  );
};
