import React from 'react';

export const LoginPage: React.FC = () => {
  return (
    <div>
      <h2 className="text-xl font-bold text-white mb-2">Welcome Back</h2>
      <p className="text-sm text-slate-400 mb-6">Enter your enterprise credentials to access the security console.</p>
      <form onSubmit={(e) => e.preventDefault()} className="space-y-4">
        <div>
          <label className="block text-xs font-semibold uppercase tracking-wider text-slate-400 mb-2">
            Work Email
          </label>
          <input
            type="email"
            placeholder="security@enterprise.com"
            className="w-full px-4 py-2.5 rounded-lg bg-slate-950 border border-slate-800 text-white focus:outline-none focus:border-emerald-500 text-sm"
          />
        </div>
        <div>
          <label className="block text-xs font-semibold uppercase tracking-wider text-slate-400 mb-2">
            Password
          </label>
          <input
            type="password"
            placeholder="••••••••••••"
            className="w-full px-4 py-2.5 rounded-lg bg-slate-950 border border-slate-800 text-white focus:outline-none focus:border-emerald-500 text-sm"
          />
        </div>
        <button
          type="submit"
          className="w-full py-2.5 px-4 bg-emerald-600 hover:bg-emerald-500 text-white font-semibold rounded-lg text-sm transition-colors shadow-lg shadow-emerald-950"
        >
          Sign In
        </button>
      </form>
    </div>
  );
};
