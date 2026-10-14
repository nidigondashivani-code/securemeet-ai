import React from 'react';
import { ShieldCheck, Video, AlertTriangle, Users } from 'lucide-react';

export const DashboardPage: React.FC = () => {
  const stats = [
    { label: 'Active Meetings Protected', value: '142', change: '+12%', icon: Video, color: 'text-emerald-400' },
    { label: 'Security Policies Enforced', value: '28', change: '100% Active', icon: ShieldCheck, color: 'text-cyan-400' },
    { label: 'Risks Prevented (24h)', value: '19', change: '-4%', icon: AlertTriangle, color: 'text-amber-400' },
    { label: 'Connected Workspace Users', value: '1,420', change: '+8%', icon: Users, color: 'text-purple-400' },
  ];

  return (
    <div className="space-y-8">
      <div>
        <h2 className="text-2xl font-bold tracking-tight text-white">Security & Governance Console</h2>
        <p className="text-sm text-slate-400 mt-1">Real-time surveillance across Google Meet, Zoom, and MS Teams.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {stats.map((stat, idx) => {
          const Icon = stat.icon;
          return (
            <div key={idx} className="p-6 rounded-xl bg-slate-900 border border-slate-800 flex flex-col justify-between">
              <div className="flex items-center justify-between mb-4">
                <span className="text-sm text-slate-400 font-medium">{stat.label}</span>
                <Icon className={`w-5 h-5 ${stat.color}`} />
              </div>
              <div>
                <div className="text-3xl font-extrabold text-white">{stat.value}</div>
                <div className="text-xs text-slate-500 mt-1">{stat.change}</div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
