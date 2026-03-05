import Link from 'next/link';

export default function Footer() {
  return (
    <footer className="border-t border-slate-200 bg-slate-50 mt-16">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 py-10">
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-8 text-sm">
          <div>
            <div className="font-bold text-slate-900 mb-3 flex items-center gap-2">
              <span className="text-xl">🐾</span> PetEntryGuide
            </div>
            <p className="text-slate-500 leading-relaxed">
              Structured import rules and travel requirements for pets worldwide.
            </p>
          </div>
          <div>
            <div className="font-semibold text-slate-700 mb-3">Guides</div>
            <ul className="space-y-2 text-slate-500">
              <li><Link href="/pet-travel-checklist" className="hover:text-brand-600">Pet Travel Checklist</Link></li>
              <li><Link href="/cost-to-bring-cat-to-usa" className="hover:text-brand-600">Cost to Bring Cat to USA</Link></li>
              <li><Link href="/pet-cargo-travel-guide" className="hover:text-brand-600">Pet Cargo Travel Guide</Link></li>
            </ul>
          </div>
          <div>
            <div className="font-semibold text-slate-700 mb-3">Rules</div>
            <ul className="space-y-2 text-slate-500">
              <li><Link href="/rabies-vaccine-requirements" className="hover:text-brand-600">Rabies Vaccine Requirements</Link></li>
              <li><Link href="/cdc-dog-import-rule" className="hover:text-brand-600">CDC Dog Import Rule</Link></li>
              <li><Link href="/usda-accredited-vet" className="hover:text-brand-600">USDA Accredited Vet</Link></li>
            </ul>
          </div>
        </div>
        <div className="border-t border-slate-200 mt-8 pt-6 text-xs text-slate-400">
          © 2026 PetEntryGuide.com — For informational purposes only. Always verify with official government sources.
        </div>
      </div>
    </footer>
  );
}
