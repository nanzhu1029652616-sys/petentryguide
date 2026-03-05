import type { Metadata } from 'next';
import Link from 'next/link';
import HeroSearch from '@/components/HeroSearch';

export const metadata: Metadata = {
  title: 'Find Pet Import Requirements Worldwide | PetEntryGuide',
  description: 'Search official import rules for traveling internationally with pets. Step-by-step guides for dogs and cats from any country.',
  alternates: { canonical: 'https://petentryguide.com' },
};

export default function HomePage() {
  return (
    <div>
      {/* Hero */}
      <section className="bg-gradient-to-b from-brand-900 to-brand-800 text-white py-20 px-4">
        <div className="max-w-3xl mx-auto text-center">
          <div className="inline-flex items-center gap-2 bg-brand-700/50 border border-brand-600 rounded-full px-4 py-1.5 text-xs font-medium mb-6 text-brand-200">
            🌍 2026 Updated Requirements
          </div>
          <h1 className="text-4xl sm:text-5xl font-bold mb-4 leading-tight">
            Find Pet Import Requirements<br />
            <span className="text-brand-300">Worldwide</span>
          </h1>
          <p className="text-brand-200 text-lg mb-10 max-w-xl mx-auto leading-relaxed">
            Search official import rules for traveling internationally with pets.
          </p>
          <HeroSearch />
        </div>
      </section>

      {/* Popular Routes */}
      <section className="max-w-5xl mx-auto px-4 sm:px-6 py-16">
        <h2 className="text-xl font-bold text-slate-900 mb-2">Popular Routes to the USA</h2>
        <p className="text-slate-500 text-sm mb-8">Click a route to view full import requirements for cats or dogs.</p>
        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-3 gap-4">
        <div key="China" className="bg-white border border-slate-200 rounded-xl p-5">
          <div className="font-semibold text-slate-800 mb-1">China <span className="text-slate-400">→</span> USA</div>
          <div className="flex gap-3 mt-3">
            <Link href="/china-to-usa-cat" className="flex-1 text-center text-xs font-medium bg-slate-50 hover:bg-brand-50 border border-slate-200 hover:border-brand-300 text-slate-700 hover:text-brand-700 py-1.5 rounded-lg transition-all">🐱 Cat</Link>
            <Link href="/china-to-usa-dog" className="flex-1 text-center text-xs font-medium bg-slate-50 hover:bg-brand-50 border border-slate-200 hover:border-brand-300 text-slate-700 hover:text-brand-700 py-1.5 rounded-lg transition-all">🐶 Dog</Link>
          </div>
        </div>
        <div key="Japan" className="bg-white border border-slate-200 rounded-xl p-5">
          <div className="font-semibold text-slate-800 mb-1">Japan <span className="text-slate-400">→</span> USA</div>
          <div className="flex gap-3 mt-3">
            <Link href="/japan-to-usa-cat" className="flex-1 text-center text-xs font-medium bg-slate-50 hover:bg-brand-50 border border-slate-200 hover:border-brand-300 text-slate-700 hover:text-brand-700 py-1.5 rounded-lg transition-all">🐱 Cat</Link>
            <Link href="/japan-to-usa-dog" className="flex-1 text-center text-xs font-medium bg-slate-50 hover:bg-brand-50 border border-slate-200 hover:border-brand-300 text-slate-700 hover:text-brand-700 py-1.5 rounded-lg transition-all">🐶 Dog</Link>
          </div>
        </div>
        <div key="UK" className="bg-white border border-slate-200 rounded-xl p-5">
          <div className="font-semibold text-slate-800 mb-1">UK <span className="text-slate-400">→</span> USA</div>
          <div className="flex gap-3 mt-3">
            <Link href="/uk-to-usa-cat" className="flex-1 text-center text-xs font-medium bg-slate-50 hover:bg-brand-50 border border-slate-200 hover:border-brand-300 text-slate-700 hover:text-brand-700 py-1.5 rounded-lg transition-all">🐱 Cat</Link>
            <Link href="/uk-to-usa-dog" className="flex-1 text-center text-xs font-medium bg-slate-50 hover:bg-brand-50 border border-slate-200 hover:border-brand-300 text-slate-700 hover:text-brand-700 py-1.5 rounded-lg transition-all">🐶 Dog</Link>
          </div>
        </div>
        <div key="Canada" className="bg-white border border-slate-200 rounded-xl p-5">
          <div className="font-semibold text-slate-800 mb-1">Canada <span className="text-slate-400">→</span> USA</div>
          <div className="flex gap-3 mt-3">
            <Link href="/canada-to-usa-cat" className="flex-1 text-center text-xs font-medium bg-slate-50 hover:bg-brand-50 border border-slate-200 hover:border-brand-300 text-slate-700 hover:text-brand-700 py-1.5 rounded-lg transition-all">🐱 Cat</Link>
            <Link href="/canada-to-usa-dog" className="flex-1 text-center text-xs font-medium bg-slate-50 hover:bg-brand-50 border border-slate-200 hover:border-brand-300 text-slate-700 hover:text-brand-700 py-1.5 rounded-lg transition-all">🐶 Dog</Link>
          </div>
        </div>
        <div key="Germany" className="bg-white border border-slate-200 rounded-xl p-5">
          <div className="font-semibold text-slate-800 mb-1">Germany <span className="text-slate-400">→</span> USA</div>
          <div className="flex gap-3 mt-3">
            <Link href="/germany-to-usa-cat" className="flex-1 text-center text-xs font-medium bg-slate-50 hover:bg-brand-50 border border-slate-200 hover:border-brand-300 text-slate-700 hover:text-brand-700 py-1.5 rounded-lg transition-all">🐱 Cat</Link>
            <Link href="/germany-to-usa-dog" className="flex-1 text-center text-xs font-medium bg-slate-50 hover:bg-brand-50 border border-slate-200 hover:border-brand-300 text-slate-700 hover:text-brand-700 py-1.5 rounded-lg transition-all">🐶 Dog</Link>
          </div>
        </div>
        <div key="India" className="bg-white border border-slate-200 rounded-xl p-5">
          <div className="font-semibold text-slate-800 mb-1">India <span className="text-slate-400">→</span> USA</div>
          <div className="flex gap-3 mt-3">
            <Link href="/india-to-usa-cat" className="flex-1 text-center text-xs font-medium bg-slate-50 hover:bg-brand-50 border border-slate-200 hover:border-brand-300 text-slate-700 hover:text-brand-700 py-1.5 rounded-lg transition-all">🐱 Cat</Link>
            <Link href="/india-to-usa-dog" className="flex-1 text-center text-xs font-medium bg-slate-50 hover:bg-brand-50 border border-slate-200 hover:border-brand-300 text-slate-700 hover:text-brand-700 py-1.5 rounded-lg transition-all">🐶 Dog</Link>
          </div>
        </div>
        </div>
      </section>

      {/* Info Strip */}
      <section className="bg-brand-50 border-y border-brand-100 py-12 px-4">
        <div className="max-w-5xl mx-auto grid grid-cols-1 sm:grid-cols-3 gap-8 text-center">
          <div>
            <div className="text-3xl mb-2">📋</div>
            <div className="font-semibold text-slate-800 mb-1">Step-by-Step Process</div>
            <p className="text-slate-500 text-sm">Every guide includes an ordered checklist of required steps.</p>
          </div>
          <div>
            <div className="text-3xl mb-2">📄</div>
            <div className="font-semibold text-slate-800 mb-1">Required Documents</div>
            <p className="text-slate-500 text-sm">Know exactly which documents to prepare before you travel.</p>
          </div>
          <div>
            <div className="text-3xl mb-2">💡</div>
            <div className="font-semibold text-slate-800 mb-1">Expert Tips</div>
            <p className="text-slate-500 text-sm">Practical advice from experienced pet travel professionals.</p>
          </div>
        </div>
      </section>

      {/* Rule Pages */}
      <section className="max-w-5xl mx-auto px-4 sm:px-6 py-16">
        <h2 className="text-xl font-bold text-slate-900 mb-6">Important Rules & Regulations</h2>
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
          <Link href="/rabies-vaccine-requirements" className="block bg-white border border-slate-200 rounded-xl p-5 hover:border-brand-300 hover:shadow-sm transition-all">
            <div className="text-2xl mb-2">💉</div>
            <div className="font-semibold text-slate-800 mb-1">Rabies Vaccine Requirements</div>
            <p className="text-slate-500 text-xs">Global vaccination rules for international pet travel.</p>
          </Link>
          <Link href="/cdc-dog-import-rule" className="block bg-white border border-slate-200 rounded-xl p-5 hover:border-brand-300 hover:shadow-sm transition-all">
            <div className="text-2xl mb-2">🏛️</div>
            <div className="font-semibold text-slate-800 mb-1">CDC Dog Import Rule</div>
            <p className="text-slate-500 text-xs">USA CDC requirements for importing dogs from abroad.</p>
          </Link>
          <Link href="/usda-accredited-vet" className="block bg-white border border-slate-200 rounded-xl p-5 hover:border-brand-300 hover:shadow-sm transition-all">
            <div className="text-2xl mb-2">🩺</div>
            <div className="font-semibold text-slate-800 mb-1">USDA Accredited Vet</div>
            <p className="text-slate-500 text-xs">Why you need a USDA-accredited vet for export health certificates.</p>
          </Link>
        </div>
      </section>
    </div>
  );
}
