import React from 'react';
import { FileText, Download } from 'lucide-react';

export const AuditLogsPage: React.FC = () => {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold tracking-tight text-white">Immutable Audit Trail</h2>
          <p className="text-sm text-slate-400 mt-1">SOC-2 Type II and ISO-27001 compliant activity logging.</p>
        </div>
        <button className="flex items-center gap-2 px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-lg text-sm font-semibold transition-colors">
          <Download className="w-4 h-4" />
          Export CSV
        </button>
      </div>

      <div className="border border-slate-800 rounded-xl bg-slate-900 p-8 text-center">
        <FileText className="w-12 h-12 text-slate-600 mx-auto mb-3" />
        <h3 className="text-lg font-medium text-slate-300">Audit logs stream ready</h3>
        <p className="text-sm text-slate-500 max-w-sm mx-auto mt-1">
          Activity events will be captured automatically as user actions and automated scans execute.
        </p>
      </div>
    </div>
  );
};
