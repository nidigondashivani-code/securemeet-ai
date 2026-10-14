import React from 'react';
import { ShieldCheck, Plus, CheckCircle2 } from 'lucide-react';

export const SecurityPoliciesPage: React.FC = () => {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold tracking-tight text-white">Security & DLP Policies</h2>
          <p className="text-sm text-slate-400 mt-1">Configure data loss prevention, attendee verification, and auto-termination rules.</p>
        </div>
        <button className="flex items-center gap-2 px-4 py-2 bg-emerald-600 hover:bg-emerald-500 text-white rounded-lg text-sm font-semibold transition-colors">
          <Plus className="w-4 h-4" />
          New Policy
        </button>
      </div>

      <div className="border border-slate-800 rounded-xl bg-slate-900 divide-y divide-slate-800">
        <div className="p-6 flex items-center justify-between">
          <div className="space-y-1">
            <div className="flex items-center gap-2">
              <span className="font-semibold text-white">Block Screen Sharing for Guests</span>
              <span className="px-2 py-0.5 text-xs rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Active</span>
            </div>
            <p className="text-sm text-slate-400">Prevents external participants from broadcasting screens unless authorized by host.</p>
          </div>
          <CheckCircle2 className="w-5 h-5 text-emerald-400" />
        </div>
      </div>
    </div>
  );
};
