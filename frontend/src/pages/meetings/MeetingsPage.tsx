import React from 'react';
import { Video, Calendar, ShieldCheck } from 'lucide-react';

export const MeetingsPage: React.FC = () => {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold tracking-tight text-white">Protected Meetings</h2>
          <p className="text-sm text-slate-400 mt-1">Manage conference security guardrails across connected integrations.</p>
        </div>
        <button className="px-4 py-2 bg-emerald-600 hover:bg-emerald-500 text-white rounded-lg text-sm font-semibold transition-colors">
          Connect Platform
        </button>
      </div>

      <div className="p-8 border border-slate-800 rounded-xl bg-slate-900/40 text-center">
        <Video className="w-12 h-12 text-slate-600 mx-auto mb-3" />
        <h3 className="text-lg font-medium text-slate-300">No active conference feeds</h3>
        <p className="text-sm text-slate-500 max-w-sm mx-auto mt-1">
          Hook into Google Meet, Zoom, or Microsoft Teams to start live DLP enforcement.
        </p>
      </div>
    </div>
  );
};
