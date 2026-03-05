export default function SummaryGrid({
  items,
}: {
  items: Array<{ label: string; value: string }>;
}) {
  return (
    <div className="grid gap-3 sm:grid-cols-2">
      {items.map((it) => (
        <div
          key={it.label}
          className="rounded-2xl border bg-white p-4 shadow-sm"
        >
          <div className="text-xs font-medium uppercase tracking-wide text-gray-500">
            {it.label}
          </div>
          <div className="mt-2 text-sm text-gray-900">{it.value}</div>
        </div>
      ))}
    </div>
  );
}
