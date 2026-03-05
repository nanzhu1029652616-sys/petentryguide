import Link from 'next/link';

export default function Navbar() {
  return (
    <header className="border-b border-slate-200 bg-white sticky top-0 z-50">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 h-14 flex items-center justify-between">
        <Link href="/" className="flex items-center gap-2 font-bold text-slate-900 text-lg">
          <span className="text-2xl">🐾</span>
          <span>PetEntryGuide</span>
        </Link>
        <nav className="flex items-center gap-6 text-sm text-slate-600">
          <Link href="/pet-travel-checklist" className="hover:text-brand-600 transition-colors">Checklist</Link>
          <Link href="/pet-cargo-travel-guide" className="hover:text-brand-600 transition-colors">Cargo Guide</Link>
          <Link href="/rabies-vaccine-requirements" className="hover:text-brand-600 transition-colors">Rabies Rules</Link>
        </nav>
      </div>
    </header>
  );
}
