import type { Metadata } from 'next';
import Link from 'next/link';

export const metadata: Metadata = {
  title: 'Pet Cargo Travel Guide – How to Ship Your Pet Safely',
  description: 'Everything you need to know about shipping your pet as cargo on international flights: crate requirements, airline policies, preparation tips, and arrival.',
  alternates: { canonical: 'https://petentryguide.com/pet-cargo-travel-guide' },
};

export default function CargoPage() {
  return (
    <div className="max-w-3xl mx-auto px-4 sm:px-6 py-12">
      <div className="mb-10">
        <div className="inline-flex items-center gap-2 text-xs font-semibold text-brand-600 bg-brand-50 border border-brand-200 rounded-full px-3 py-1 mb-4">✈️ Practical Guide</div>
        <h1 className="text-3xl font-bold text-slate-900 mb-3">Pet Cargo Travel Guide</h1>
        <p className="text-slate-500 leading-relaxed">For large pets, long-haul flights, or airlines that don't allow cabin pets, cargo is the standard option. This guide covers everything you need to prepare for safe cargo travel.</p>
      </div>

      <div className="space-y-8">
        <section className="bg-white border border-slate-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-slate-900 mb-3">IATA Crate Requirements</h2>
          <p className="text-slate-600 text-sm mb-4">All cargo pets must travel in an <strong>IATA Live Animal Regulations</strong>-compliant crate. Requirements include:</p>
          <ul className="space-y-2 text-slate-600 text-sm">
            <li className="flex gap-2"><span className="text-brand-500">→</span> Rigid walls with proper ventilation on at least 3 sides</li>
            <li className="flex gap-2"><span className="text-brand-500">→</span> Pet must be able to stand, turn around, and lie down naturally</li>
            <li className="flex gap-2"><span className="text-brand-500">→</span> Water and food containers accessible from outside</li>
            <li className="flex gap-2"><span className="text-brand-500">→</span> "Live Animal" labels on top and sides</li>
            <li className="flex gap-2"><span className="text-brand-500">→</span> Absorbent bedding inside</li>
          </ul>
        </section>

        <section className="bg-white border border-slate-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-slate-900 mb-3">How to Prepare Your Pet</h2>
          <ul className="space-y-2 text-slate-600 text-sm">
            <li className="flex gap-2"><span className="text-emerald-500">✓</span> Begin crate training 4–6 weeks before travel</li>
            <li className="flex gap-2"><span className="text-emerald-500">✓</span> Fast the pet 4–6 hours before the flight</li>
            <li className="flex gap-2"><span className="text-emerald-500">✓</span> Exercise the pet well before drop-off</li>
            <li className="flex gap-2"><span className="text-emerald-500">✓</span> Do NOT sedate pets for air travel (increases health risk)</li>
            <li className="flex gap-2"><span className="text-emerald-500">✓</span> Attach a familiar item (blanket, toy) for comfort</li>
          </ul>
        </section>

        <section className="bg-amber-50 border border-amber-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-amber-900 mb-3">⚠️ Important Warnings</h2>
          <ul className="space-y-2 text-amber-800 text-sm">
            <li className="flex gap-2"><span>→</span> Many airlines embargo cargo pets during extreme temperatures</li>
            <li className="flex gap-2"><span>→</span> Snub-nosed breeds (bulldogs, persians) are often restricted from cargo</li>
            <li className="flex gap-2"><span>→</span> Cargo is temperature-controlled but not identical to cabin conditions</li>
          </ul>
        </section>

        <section className="bg-white border border-slate-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-slate-900 mb-3">Related Guides</h2>
          <div className="space-y-2">
            <Link href="/pet-travel-checklist" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ Pet Travel Checklist</Link>
            <Link href="/cost-to-bring-cat-to-usa" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ Cost to Bring a Cat to USA</Link>
          </div>
        </section>
      </div>
    </div>
  );
}
