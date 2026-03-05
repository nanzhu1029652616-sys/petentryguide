import type { Metadata } from 'next';
import Link from 'next/link';

export const metadata: Metadata = {
  title: 'CDC Dog Import Rule – USA Requirements Explained',
  description: 'Full explanation of the CDC dog import rule for bringing dogs into the United States, including the Dog Import Form, CDC-approved facilities, and exemptions.',
  alternates: { canonical: 'https://petentryguide.com/cdc-dog-import-rule' },
};

export default function CDCPage() {
  return (
    <div className="max-w-3xl mx-auto px-4 sm:px-6 py-12">
      <div className="mb-8">
        <div className="inline-flex items-center gap-2 text-xs font-semibold text-brand-600 bg-brand-50 border border-brand-200 rounded-full px-3 py-1 mb-4">🏛️ Rule</div>
        <h1 className="text-3xl font-bold text-slate-900 mb-3">CDC Dog Import Rule</h1>
        <p className="text-slate-500 leading-relaxed">The CDC (Centers for Disease Control and Prevention) regulates the importation of all dogs into the United States. This rule applies to every dog, regardless of origin.</p>
      </div>

      <div className="space-y-8">
        <section className="bg-white border border-slate-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-slate-900 mb-3">What is the CDC Dog Import Form?</h2>
          <p className="text-slate-600 leading-relaxed mb-3">Since August 2024, all dogs entering the USA must have their owner complete the <strong>CDC Dog Import Form</strong> online before travel. Upon submission, you receive a unique <strong>CDC Import Code</strong> via email which must be presented at the port of entry.</p>
          <div className="bg-slate-50 border border-slate-200 rounded-lg p-4 text-sm text-slate-700">
            Submit at: <strong>cdc.gov/importation/dogs</strong>
          </div>
        </section>

        <section className="bg-white border border-slate-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-slate-900 mb-3">High-Risk vs Low-Risk Countries</h2>
          <p className="text-slate-600 text-sm mb-4">The CDC classifies countries as high-risk or low-risk for dog rabies. Dogs from high-risk countries (including China, India, Mexico, and many others) must be vaccinated at a <strong>CDC-approved facility</strong>. Dogs from low-risk countries (UK, EU, Japan, Australia, Canada) follow a simpler process.</p>
          <div className="grid grid-cols-2 gap-4 text-sm">
            <div className="bg-emerald-50 border border-emerald-200 rounded-lg p-4">
              <div className="font-semibold text-emerald-800 mb-2">Low-Risk Countries</div>
              <p className="text-emerald-700">UK, EU, Japan, Australia, Canada, New Zealand, Singapore, South Korea</p>
            </div>
            <div className="bg-amber-50 border border-amber-200 rounded-lg p-4">
              <div className="font-semibold text-amber-800 mb-2">High-Risk Countries</div>
              <p className="text-amber-700">China, India, Mexico, Brazil, and many others — check CDC website for full list</p>
            </div>
          </div>
        </section>

        <section className="bg-amber-50 border border-amber-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-amber-900 mb-3">⚠️ Common Mistakes</h2>
          <ul className="space-y-2 text-amber-800 text-sm">
            <li className="flex gap-2"><span>→</span> Not completing the CDC form before boarding</li>
            <li className="flex gap-2"><span>→</span> Using a non-CDC-approved facility for high-risk countries</li>
            <li className="flex gap-2"><span>→</span> Missing the CDC Import Code at the port of entry</li>
          </ul>
        </section>

        <section className="bg-white border border-slate-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-slate-900 mb-3">Related Guides</h2>
          <div className="space-y-2">
            <Link href="/china-to-usa-dog" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ Dog Import: China to USA</Link>
            <Link href="/india-to-usa-dog" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ Dog Import: India to USA</Link>
            <Link href="/rabies-vaccine-requirements" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ Rabies Vaccine Requirements</Link>
          </div>
        </section>
      </div>
    </div>
  );
}
