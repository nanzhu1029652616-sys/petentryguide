import type { Metadata } from 'next';
import Link from 'next/link';

export const metadata: Metadata = {
  title: 'Cost to Bring a Cat to the USA – 2026 Breakdown',
  description: 'Complete cost breakdown for bringing a cat to the United States from any country: vet fees, airline fees, health certificates, and more.',
  alternates: { canonical: 'https://petentryguide.com/cost-to-bring-cat-to-usa' },
};

export default function CostPage() {
  const costs = [
    { item: 'ISO Microchip (if needed)', low: 30, high: 80 },
    { item: 'Rabies Vaccination', low: 20, high: 100 },
    { item: 'Export Health Certificate (Vet Fee)', low: 100, high: 350 },
    { item: 'Government Endorsement Fee', low: 30, high: 150 },
    { item: 'Airline Pet-in-Cabin Fee', low: 95, high: 200 },
    { item: 'Airline Cargo Fee', low: 200, high: 600 },
    { item: 'IATA-compliant Carrier/Crate', low: 40, high: 200 },
    { item: 'Pet Relocation Service (optional)', low: 500, high: 3000 },
  ];

  const totalLow  = costs.reduce((s, c) => s + c.low, 0);
  const totalHigh = costs.reduce((s, c) => s + c.high, 0);

  return (
    <div className="max-w-3xl mx-auto px-4 sm:px-6 py-12">
      <div className="mb-10">
        <div className="inline-flex items-center gap-2 text-xs font-semibold text-brand-600 bg-brand-50 border border-brand-200 rounded-full px-3 py-1 mb-4">💰 Practical Guide</div>
        <h1 className="text-3xl font-bold text-slate-900 mb-3">Cost to Bring a Cat to the USA</h1>
        <p className="text-slate-500 leading-relaxed">Bringing a cat to the USA involves multiple fees. Here is a comprehensive 2026 cost breakdown to help you budget for your pet's international move.</p>
      </div>

      <div className="bg-white border border-slate-200 rounded-xl overflow-hidden mb-8">
        <table className="w-full text-sm">
          <thead>
            <tr className="bg-slate-50 border-b border-slate-200">
              <th className="text-left px-5 py-3 font-semibold text-slate-600">Item</th>
              <th className="text-right px-5 py-3 font-semibold text-slate-600">Low (USD)</th>
              <th className="text-right px-5 py-3 font-semibold text-slate-600">High (USD)</th>
            </tr>
          </thead>
          <tbody>
            {costs.map((c, i) => (
              <tr key={i} className="border-b border-slate-100 hover:bg-slate-50">
                <td className="px-5 py-3 text-slate-700">{c.item}</td>
                <td className="px-5 py-3 text-right text-slate-700">${c.low}</td>
                <td className="px-5 py-3 text-right text-slate-700">${c.high}</td>
              </tr>
            ))}
            <tr className="bg-brand-50 font-bold">
              <td className="px-5 py-3 text-brand-900">Estimated Total</td>
              <td className="px-5 py-3 text-right text-brand-900">${totalLow.toLocaleString()}</td>
              <td className="px-5 py-3 text-right text-brand-900">${totalHigh.toLocaleString()}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div className="bg-amber-50 border border-amber-200 rounded-xl p-6 mb-8">
        <h2 className="font-bold text-amber-900 mb-2">💡 Tips to Reduce Costs</h2>
        <ul className="space-y-2 text-amber-800 text-sm">
          <li className="flex gap-2"><span>→</span> Book flights directly with airlines that allow pets in cabin (avoid cargo fees)</li>
          <li className="flex gap-2"><span>→</span> Use a USDA-accredited vet for the health certificate to avoid rebooking fees</li>
          <li className="flex gap-2"><span>→</span> Prepare all documents yourself instead of using a full relocation service</li>
        </ul>
      </div>

      <div className="bg-white border border-slate-200 rounded-xl p-6">
        <h2 className="font-bold text-slate-900 mb-3">Related Guides</h2>
        <div className="space-y-2">
          <Link href="/china-to-usa-cat" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ Cat Import: China to USA</Link>
          <Link href="/pet-travel-checklist" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ Pet Travel Checklist</Link>
          <Link href="/pet-cargo-travel-guide" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ Pet Cargo Travel Guide</Link>
        </div>
      </div>
    </div>
  );
}
