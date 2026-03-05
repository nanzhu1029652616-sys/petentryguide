interface Item {
  label: string;
  value: string;
  status?: 'ok' | 'warn' | 'neutral';
}

export default function SummaryGrid({ items }: { items: Item[] }) {
  const color = (s?: string) => {
    if (s === 'ok')   return 'text-emerald-700 bg-emerald-50 border-emerald-200';
    if (s === 'warn') return 'text-amber-700 bg-amber-50 border-amber-200';
    return 'text-slate-700 bg-slate-50 border-slate-200';
  };
  return (
    <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
      {items.map(item => (
        <div key={item.label} className={`rounded-xl border p-4 ${color(item.status)}`}>
          <div className="text-xs font-semibold uppercase tracking-wide opacity-70 mb-1">{item.label}</div>
          <div className="text-sm font-bold">{item.value}</div>
        </div>
      ))}
    </div>
  );
}
