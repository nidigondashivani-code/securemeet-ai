import React from 'react';
import { Settings as SettingsIcon } from 'lucide-react';

export const SettingsPage: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-2xl font-bold tracking-tight text-white">System Settings</h2>
        <p className="text-sm text-slate-400 mt-1">Configure tenant preferences, OAuth credentials, and AI model parameters.</p>
      </div>

      <div className="border border-slate-800 rounded-xl bg-slate-900 p-8 text-center">
        <SettingsIcon className="w-12 h-12 text-slate-600 mx-auto mb-3" />
        <h3 className="text-lg font-medium text-slate-300">Configuration Console</h3>
        <p className="text-sm text-slate-500 max-w-sm mx-auto mt-1">
          Tenant governance options and integration tokens can be managed here.
        </p>
      </div>
    </div>
  );
};
