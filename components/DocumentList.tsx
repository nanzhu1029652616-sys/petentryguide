export default function DocumentList({ items }: { items: string[] }) {
  return (
    <ul className="list-disc space-y-2 pl-5 text-gray-800">
      {items.map((d, idx) => (
        <li key={idx}>{d}</li>
      ))}
    </ul>
  );
}
