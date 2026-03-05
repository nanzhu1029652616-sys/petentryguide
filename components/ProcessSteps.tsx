export default function ProcessSteps({ steps }: { steps: string[] }) {
  return (
    <ol className="space-y-3">
      {steps.map((s, idx) => (
        <li key={idx} className="rounded-2xl border bg-white p-4 shadow-sm">
          <div className="text-sm font-semibold">
            Step {idx + 1} <span className="font-normal text-gray-500">–</span>{" "}
            <span className="font-normal">{s}</span>
          </div>
        </li>
      ))}
    </ol>
  );
}
