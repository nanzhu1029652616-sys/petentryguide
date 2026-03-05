import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { getAllSlugs, getRouteBySlug } from '@/lib/getRoutes';
import SummaryGrid from '@/components/SummaryGrid';
import ProcessSteps from '@/components/ProcessSteps';
import DocumentList from '@/components/DocumentList';
import Breadcrumb from '@/components/Breadcrumb';

export async function generateStaticParams() {
  const slugs = getAllSlugs();
  return slugs.map(slug => ({ slug }));
}

export async function generateMetadata({ params }: { params: { slug: string } }): Promise<Metadata> {
  const route = getRouteBySlug(params.slug);
  if (!route) return { title: 'Not Found' };
  return {
    title: `${route.title} | PetEntryGuide`,
    description: route.summary,
    alternates: { canonical: `https://petentryguide.com/${route.slug}` },
    openGraph: {
      title: route.title,
      description: route.summary,
      url: `https://petentryguide.com/${route.slug}`,
      type: 'article',
    },
  };
}

export default function RouteGuidePage({ params }: { params: { slug: string } }) {
  const route = getRouteBySlug(params.slug);
  if (!route) notFound();

  const summaryItems = [
    {
      label: 'Minimum Age',
      value: route.min_age,
      status: 'neutral' as const,
    },
    {
      label: 'Microchip',
      value: route.microchip.includes('required') || route.microchip.includes('Required')
        ? 'Required' : route.microchip,
      status: (route.microchip.toLowerCase().includes('required') ? 'warn' : 'neutral') as const,
    },
    {
      label: 'Rabies Vaccine',
      value: route.rabies_vaccine,
      status: (route.rabies_vaccine.toLowerCase().includes('required') ? 'warn' : 'ok') as const,
    },
    {
      label: 'Quarantine',
      value: route.quarantine,
      status: (route.quarantine.toLowerCase() === 'no' ? 'ok' : 'warn') as const,
    },
  ];

  const petEmoji = route.pet_type === 'cat' ? '🐱' : '🐶';

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 py-10">
      <Breadcrumb crumbs={[
        { label: 'Home', href: '/' },
        { label: route.from_country },
        { label: route.to_country },
        { label: route.pet_type.charAt(0).toUpperCase() + route.pet_type.slice(1) },
      ]} />

      {/* Header */}
      <div className="mb-8">
        <div className="inline-flex items-center gap-2 text-xs font-semibold text-brand-600 bg-brand-50 border border-brand-200 rounded-full px-3 py-1 mb-4">
          {petEmoji} {route.from_country} → {route.to_country}
        </div>
        <h1 className="text-3xl sm:text-4xl font-bold text-slate-900 mb-3 leading-tight">
          {route.title}
        </h1>
        <p className="text-slate-500 text-base leading-relaxed max-w-2xl">{route.summary}</p>
      </div>

      {/* Quick Summary */}
      <section className="mb-10">
        <h2 className="text-lg font-bold text-slate-900 mb-4">Quick Requirements Summary</h2>
        <SummaryGrid items={summaryItems} />
      </section>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Main Content */}
        <div className="lg:col-span-2 space-y-10">

          {/* Process */}
          <section>
            <h2 className="text-lg font-bold text-slate-900 mb-4">Step-by-Step Process</h2>
            <div className="bg-white border border-slate-200 rounded-xl p-6">
              <ProcessSteps steps={route.process_steps} />
            </div>
          </section>

          {/* Documents */}
          <section>
            <h2 className="text-lg font-bold text-slate-900 mb-4">Required Documents</h2>
            <div className="bg-white border border-slate-200 rounded-xl p-6">
              <DocumentList documents={route.required_documents} />
            </div>
          </section>

          {/* Tips */}
          {route.tips.length > 0 && (
            <section>
              <h2 className="text-lg font-bold text-slate-900 mb-4">Expert Tips</h2>
              <div className="bg-amber-50 border border-amber-200 rounded-xl p-6 space-y-3">
                {route.tips.map((tip, i) => (
                  <div key={i} className="flex gap-3 text-sm text-amber-900">
                    <span className="text-amber-500 flex-shrink-0 mt-0.5">💡</span>
                    <span>{tip}</span>
                  </div>
                ))}
              </div>
            </section>
          )}
        </div>

        {/* Sidebar */}
        <div className="space-y-6">

          {/* Vaccines */}
          <div className="bg-white border border-slate-200 rounded-xl p-5">
            <h3 className="font-bold text-slate-800 mb-3 text-sm">💉 Vaccination Requirements</h3>
            <ul className="space-y-2">
              {route.vaccines.map((v, i) => (
                <li key={i} className="text-sm text-slate-700 flex items-start gap-2">
                  <span className="text-emerald-500 mt-0.5">✓</span> {v}
                </li>
              ))}
            </ul>
          </div>

          {/* Travel Methods */}
          <div className="bg-white border border-slate-200 rounded-xl p-5">
            <h3 className="font-bold text-slate-800 mb-3 text-sm">✈️ Travel Methods</h3>
            <ul className="space-y-2">
              {route.travel_methods.map((m, i) => (
                <li key={i} className="text-sm text-slate-700 flex items-start gap-2">
                  <span className="text-brand-400 mt-0.5">→</span> {m}
                </li>
              ))}
            </ul>
          </div>

          {/* Disclaimer */}
          <div className="bg-slate-50 border border-slate-200 rounded-xl p-5 text-xs text-slate-500 leading-relaxed">
            ⚠️ Requirements change frequently. Always verify with official government sources before travel.
          </div>
        </div>
      </div>
    </div>
  );
}
