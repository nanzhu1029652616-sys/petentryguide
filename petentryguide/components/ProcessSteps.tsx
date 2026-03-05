export default function ProcessSteps({ steps }: { steps: string[] }) {
  return (
    <ol className="space-y-3">
      {steps.map((step, i) => (
        <li key={i} className="flex gap-4 items-start">
          <span className="flex-shrink-0 w-7 h-7 rounded-full bg-brand-600 text-white text-xs font-bold flex items-center justify-center mt-0.5">
            {i + 1}
          </span>
          <span className="text-slate-700 text-sm leading-relaxed pt-1">{step}</span>
        </li>
      ))}
    </ol>
  );
}
