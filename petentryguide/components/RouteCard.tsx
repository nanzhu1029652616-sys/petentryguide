import Link from 'next/link';

interface RouteCardProps {
  from: string;
  to: string;
  petType: string;
  slug: string;
}

export default function RouteCard({ from, to, petType, slug }: RouteCardProps) {
  const emoji = petType === 'cat' ? '🐱' : '🐶';
  return (
    <Link href={`/${slug}`}
      className="block bg-white border border-slate-200 rounded-xl p-5 hover:border-brand-400 hover:shadow-md transition-all duration-150 group"
    >
      <div className="flex items-center gap-3 mb-2">
        <span className="text-2xl">{emoji}</span>
        <span className="font-semibold text-slate-800 capitalize">{petType}</span>
      </div>
      <div className="text-sm text-slate-500">
        <span className="font-medium text-slate-700">{from}</span>
        <span className="mx-2 text-slate-400">→</span>
        <span className="font-medium text-slate-700">{to}</span>
      </div>
      <div className="mt-3 text-xs text-brand-600 font-medium group-hover:underline">View requirements →</div>
    </Link>
  );
}
