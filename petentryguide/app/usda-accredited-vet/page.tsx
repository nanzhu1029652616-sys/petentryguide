import type { Metadata } from 'next';
import Link from 'next/link';

export const metadata: Metadata = {
  title: 'USDA Accredited Vet – Export Health Certificates Explained',
  description: 'Learn what a USDA-accredited veterinarian is, why you need one for international pet travel, and how to find one.',
  alternates: { canonical: 'https://petentryguide.com/usda-accredited-vet' },
};

export default function USDAPage() {
  return (
    <div className="max-w-3xl mx-auto px-4 sm:px-6 py-12">
      <div className="mb-8">
        <div className="inline-flex items-center gap-2 text-xs font-semibold text-brand-600 bg-brand-50 border border-brand-200 rounded-full px-3 py-1 mb-4">🩺 Rule</div>
        <h1 className="text-3xl font-bold text-slate-900 mb-3">USDA Accredited Vet</h1>
        <p className="text-slate-500 leading-relaxed">When exporting a pet from the United States, or when destination countries require it, you need an Export Health Certificate (EHC) signed by a USDA-accredited veterinarian and endorsed by the USDA APHIS.</p>
      </div>

      <div className="space-y-8">
        <section className="bg-white border border-slate-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-slate-900 mb-3">What is a USDA-Accredited Vet?</h2>
          <p className="text-slate-600 leading-relaxed">A USDA-accredited veterinarian is a private veterinarian authorized by the USDA Animal and Plant Health Inspection Service (APHIS) to certify animals for interstate and international travel. Not all vets are accredited — you must specifically seek one with USDA accreditation.</p>
        </section>

        <section className="bg-white border border-slate-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-slate-900 mb-3">When Do You Need One?</h2>
          <ul className="space-y-2 text-slate-600 text-sm">
            <li className="flex gap-2"><span className="text-brand-500">→</span> Exporting a pet from the USA to another country</li>
            <li className="flex gap-2"><span className="text-brand-500">→</span> Certain destination countries require USDA-backed health certificates</li>
            <li className="flex gap-2"><span className="text-brand-500">→</span> Getting a certificate endorsed by USDA APHIS (required by many countries)</li>
          </ul>
        </section>

        <section className="bg-white border border-slate-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-slate-900 mb-3">How to Find a USDA-Accredited Vet</h2>
          <p className="text-slate-600 text-sm leading-relaxed mb-3">Visit the USDA APHIS website and use the Accredited Vet search tool. Search by state and zip code. Always call ahead to confirm the vet is familiar with international health certificate requirements.</p>
          <div className="bg-slate-50 border border-slate-200 rounded-lg p-4 text-sm text-slate-700">
            Search at: <strong>aphis.usda.gov</strong> → Veterinary Accreditation
          </div>
        </section>

        <section className="bg-white border border-slate-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-slate-900 mb-3">Related Guides</h2>
          <div className="space-y-2">
            <Link href="/pet-travel-checklist" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ Pet Travel Checklist</Link>
            <Link href="/cdc-dog-import-rule" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ CDC Dog Import Rule</Link>
          </div>
        </section>
      </div>
    </div>
  );
}
