'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';

const FROM_COUNTRIES = [
  'Australia','Brazil','Canada','China','France','Germany',
  'India','Japan','Mexico','New Zealand','Singapore','South Korea','UK'
];
const TO_COUNTRIES = ['USA'];
const PET_TYPES    = ['cat','dog'];

export default function HeroSearch() {
  const router = useRouter();
  const [from, setFrom] = useState('');
  const [to, setTo]     = useState('USA');
  const [pet, setPet]   = useState('');
  const [error, setError] = useState('');

  const handleSearch = () => {
    if (!from || !to || !pet) {
      setError('Please select all three options.');
      return;
    }
    setError('');
    const slug = `${from.toLowerCase().replace(/\s+/g,'-')}-to-${to.toLowerCase()}-${pet}`;
    router.push(`/${slug}`);
  };

  return (
    <div className="bg-white rounded-2xl shadow-lg border border-slate-200 p-8 max-w-2xl mx-auto">
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-4">
        <div>
          <label className="block text-xs font-semibold text-slate-500 mb-1 uppercase tracking-wide">From Country</label>
          <select
            value={from}
            onChange={e => setFrom(e.target.value)}
            className="w-full border border-slate-200 rounded-lg px-3 py-2.5 text-slate-800 bg-slate-50 focus:outline-none focus:ring-2 focus:ring-brand-500 text-sm"
          >
            <option value="">Select country</option>
            {FROM_COUNTRIES.map(c => <option key={c} value={c}>{c}</option>)}
          </select>
        </div>
        <div>
          <label className="block text-xs font-semibold text-slate-500 mb-1 uppercase tracking-wide">To Country</label>
          <select
            value={to}
            onChange={e => setTo(e.target.value)}
            className="w-full border border-slate-200 rounded-lg px-3 py-2.5 text-slate-800 bg-slate-50 focus:outline-none focus:ring-2 focus:ring-brand-500 text-sm"
          >
            {TO_COUNTRIES.map(c => <option key={c} value={c}>{c}</option>)}
          </select>
        </div>
        <div>
          <label className="block text-xs font-semibold text-slate-500 mb-1 uppercase tracking-wide">Pet Type</label>
          <select
            value={pet}
            onChange={e => setPet(e.target.value)}
            className="w-full border border-slate-200 rounded-lg px-3 py-2.5 text-slate-800 bg-slate-50 focus:outline-none focus:ring-2 focus:ring-brand-500 text-sm capitalize"
          >
            <option value="">Select pet</option>
            {PET_TYPES.map(p => <option key={p} value={p} className="capitalize">{p.charAt(0).toUpperCase()+p.slice(1)}</option>)}
          </select>
        </div>
      </div>
      {error && <p className="text-red-500 text-sm mb-3">{error}</p>}
      <button
        onClick={handleSearch}
        className="w-full bg-brand-600 hover:bg-brand-700 text-white font-semibold py-3 px-6 rounded-xl transition-colors duration-150 text-sm"
      >
        Search Requirements →
      </button>
    </div>
  );
}
