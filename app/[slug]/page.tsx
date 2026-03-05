import { notFound } from "next/navigation";
import Link from "next/link";
import {
  getAllRouteSlugs,
  getRouteBySlug,
} from "@/lib/getRoutes";
import SummaryGrid from "@/components/SummaryGrid";
import ProcessSteps from "@/components/ProcessSteps";
import DocumentList from "@/components/DocumentList";

type PageProps = {
  params: { slug: string };
};

export function generateStaticParams() {
  return getAllRouteSlugs().map((slug) => ({ slug }));
}

export function generateMetadata({ params }: PageProps) {
  const route = getRouteBySlug(params.slug);
  if (!route) return {};

  const title = `Bring a ${route.pet_type.toUpperCase()} from ${route.from_country} to ${route.to_country} (2026 Import Requirements)`;
  const description = route.summary;
  const canonical = `https://petentryguide.com/${route.slug}`;

  return {
    title,
    description,
    alternates: { canonical },
  };
}

function Breadcrumb({
  from,
  to,
  pet,
}: {
  from: string;
  to: string;
  pet: string;
}) {
  return (
    <nav className="text-sm text-gray-600">
      <Link className="hover:underline" href="/">
        Home
      </Link>
      <span className="mx-2">›</span>
      <span>{from}</span>
      <span className="mx-2">›</span>
      <span>{to}</span>
      <span className="mx-2">›</span>
      <span className="capitalize">{pet}</span>
    </nav>
  );
}

export default function RouteGuidePage({ params }: PageProps) {
  const route = getRouteBySlug(params.slug);
  if (!route) notFound();

  return (
    <main className="mx-auto max-w-3xl px-4 py-10">
      <Breadcrumb
        from={route.from_country}
        to={route.to_country}
        pet={route.pet_type}
      />

      <header className="mt-4">
        <h1 className="text-2xl font-semibold tracking-tight">
          {route.title}
        </h1>
        <p className="mt-2 text-gray-700">{route.summary}</p>
      </header>

      <section className="mt-8">
        <h2 className="text-lg font-semibold">Quick requirements summary</h2>
        <div className="mt-3">
          <SummaryGrid
            items={[
              { label: "Minimum Age", value: route.min_age },
              { label: "Microchip", value: route.microchip },
              { label: "Rabies Requirement", value: route.rabies_vaccine },
              { label: "Quarantine", value: route.quarantine },
            ]}
          />
        </div>
      </section>

      <section className="mt-8">
        <h2 className="text-lg font-semibold">Step-by-step process</h2>
        <div className="mt-3">
          <ProcessSteps steps={route.process_steps} />
        </div>
      </section>

      <section className="mt-8">
        <h2 className="text-lg font-semibold">Required documents</h2>
        <div className="mt-3">
          <DocumentList items={route.required_documents} />
        </div>
      </section>

      <section className="mt-8">
        <h2 className="text-lg font-semibold">Vaccination requirements</h2>
        <div className="mt-3">
          <DocumentList items={route.vaccines} />
        </div>
      </section>

      <section className="mt-8">
        <h2 className="text-lg font-semibold">Travel methods</h2>
        <div className="mt-3">
          <DocumentList items={route.travel_methods} />
        </div>
      </section>

      <section className="mt-8 rounded-2xl border bg-amber-50 p-5">
        <h2 className="text-lg font-semibold">Expert tips</h2>
        <ul className="mt-3 list-disc space-y-2 pl-5 text-gray-800">
          {route.tips.map((t, idx) => (
            <li key={idx}>{t}</li>
          ))}
        </ul>
      </section>

      <footer className="mt-10 border-t pt-6 text-sm text-gray-500">
        <p>
          This page is a structured guide. Always confirm the latest official
          regulations before travel.
        </p>
      </footer>
    </main>
  );
}
