import type { Metadata } from 'next';
import Link from 'next/link';

export const metadata: Metadata = {
  title: 'Rabies Vaccine Requirements for International Pet Travel',
  description: 'Learn when and why a rabies vaccine is required to travel internationally with your pet, common mistakes, and which countries require it.',
  alternates: { canonical: 'https://petentryguide.com/rabies-vaccine-requirements' },
};

export default function RabiesPage() {
  return (
    <div className="max-w-3xl mx-auto px-4 sm:px-6 py-12">
      <div className="mb-8">
        <div className="inline-flex items-center gap-2 text-xs font-semibold text-brand-600 bg-brand-50 border border-brand-200 rounded-full px-3 py-1 mb-4">💉 Rule</div>
        <h1 className="text-3xl font-bold text-slate-900 mb-3">Rabies Vaccine Requirements</h1>
        <p className="text-slate-500 leading-relaxed">A rabies vaccination is one of the most universally required documents when importing pets internationally. This guide explains when it is mandatory, what proof is needed, and common mistakes to avoid.</p>
      </div>

      <div className="prose-sm max-w-none space-y-8">
        <section className="bg-white border border-slate-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-slate-900 mb-3">When is Rabies Vaccination Required?</h2>
          <p className="text-slate-600 leading-relaxed mb-3">The United States requires all imported dogs to have a valid rabies vaccination. For cats, it is strongly recommended and required by many airlines. Any country classified as high-risk for dog rabies by the CDC requires vaccination at a <strong>CDC-approved facility</strong>.</p>
          <ul className="space-y-2 text-slate-600 text-sm">
            <li className="flex gap-2"><span className="text-emerald-500">✓</span> Always required for dogs entering the USA</li>
            <li className="flex gap-2"><span className="text-emerald-500">✓</span> Required before microchipping is complete (chip must come first)</li>
            <li className="flex gap-2"><span className="text-emerald-500">✓</span> Booster shots must be within validity period</li>
          </ul>
        </section>

        <section className="bg-white border border-slate-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-slate-900 mb-3">What Proof is Needed?</h2>
          <p className="text-slate-600 leading-relaxed mb-3">You must carry an official rabies vaccination certificate issued by a licensed veterinarian. It should include:</p>
          <ul className="space-y-1 text-slate-600 text-sm list-disc list-inside">
            <li>Pet name, species, breed, and microchip number</li>
            <li>Vaccine brand, serial number, and expiry date</li>
            <li>Veterinarian's license number and signature</li>
            <li>Date of vaccination</li>
          </ul>
        </section>

        <section className="bg-amber-50 border border-amber-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-amber-900 mb-3">⚠️ Common Mistakes</h2>
          <ul className="space-y-2 text-amber-800 text-sm">
            <li className="flex gap-2"><span>→</span> Vaccinating before microchipping (vaccine won't be linked to pet ID)</li>
            <li className="flex gap-2"><span>→</span> Using an expired vaccine certificate</li>
            <li className="flex gap-2"><span>→</span> Not vaccinating at a CDC-approved facility when traveling from high-risk countries</li>
            <li className="flex gap-2"><span>→</span> Missing booster shots for pets with prior vaccinations</li>
          </ul>
        </section>

        <section className="bg-white border border-slate-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-slate-900 mb-3">Related Guides</h2>
          <div className="space-y-2">
            <Link href="/china-to-usa-dog" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ Dog Import: China to USA</Link>
            <Link href="/india-to-usa-dog" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ Dog Import: India to USA</Link>
            <Link href="/cdc-dog-import-rule" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ CDC Dog Import Rule Explained</Link>
          </div>
        </section>
      </div>
    </div>
  );
}
