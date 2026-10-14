import React from 'react';
import { BarChart3 } from 'lucide-react';

export const AnalyticsPage: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-2xl font-bold tracking-tight text-white">Governance Analytics</h2>
        <p className="text-sm text-slate-400 mt-1">Cross-platform trends, violation frequencies, and risk posture analysis.</p>
      </div>

      <div className="border border-slate-800 rounded-xl bg-slate-900 p-8 text-center">
        <BarChart3 className="w-12 h-12 text-slate-600 mx-auto mb-3" />
        <h3 className="text-lg font-medium text-slate-300">Analytics Engine Ready</h3>
        <p className="text-sm text-slate-500 max-w-sm mx-auto mt-1">
          Telemetry aggregates will appear here once meeting events begin processing.
        </p>
      </div>
    </div>
  );
};
