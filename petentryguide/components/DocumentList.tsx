export default function DocumentList({ documents }: { documents: string[] }) {
  return (
    <ul className="space-y-2">
      {documents.map((doc, i) => (
        <li key={i} className="flex items-start gap-3 text-sm text-slate-700">
          <span className="text-brand-500 mt-0.5">📄</span>
          <span>{doc}</span>
        </li>
      ))}
    </ul>
  );
}
