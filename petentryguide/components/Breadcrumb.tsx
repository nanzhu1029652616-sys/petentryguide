import Link from 'next/link';

interface Crumb {
  label: string;
  href?: string;
}

export default function Breadcrumb({ crumbs }: { crumbs: Crumb[] }) {
  return (
    <nav className="text-sm text-slate-500 mb-6 flex flex-wrap gap-1 items-center">
      {crumbs.map((crumb, i) => (
        <span key={i} className="flex items-center gap-1">
          {i > 0 && <span className="text-slate-300">›</span>}
          {crumb.href
            ? <Link href={crumb.href} className="hover:text-brand-600 transition-colors">{crumb.label}</Link>
            : <span className="text-slate-800 font-medium">{crumb.label}</span>
          }
        </span>
      ))}
    </nav>
  );
}
