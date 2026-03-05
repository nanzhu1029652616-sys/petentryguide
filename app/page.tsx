import { getAllRoutes } from "@/lib/getRoutes";
import HeroSearch from "@/components/HeroSearch";
import RouteCard from "@/components/RouteCard";

export const metadata = {
  title: "PetEntryGuide — Find Pet Import Requirements Worldwide",
  description:
    "Search structured import rules for traveling internationally with pets. Compare requirements by route and pet type.",
  alternates: { canonical: "https://petentryguide.com/" },
};

function uniqSorted(values: string[]) {
  return Array.from(new Set(values)).sort((a, b) => a.localeCompare(b));
}

export default function HomePage() {
  const routes = getAllRoutes();

  const fromCountries = uniqSorted(routes.map((r) => r.from_country));
  const toCountries = uniqSorted(routes.map((r) => r.to_country));
  const petTypes = uniqSorted(routes.map((r) => r.pet_type));

  // Popular routes per spec (cards link to cat/dog if available)
  const popularPairs: Array<{ from: string; to: string }> = [
    { from: "China", to: "USA" },
    { from: "China", to: "Canada" },
    { from: "UK", to: "USA" },
    { from: "Japan", to: "USA" },
  ];

  const popular = popularPairs.map((p) => {
    const cat = routes.find(
      (r) =>
        r.from_country === p.from &&
        r.to_country === p.to &&
        r.pet_type.toLowerCase() === "cat"
    );
    const dog = routes.find(
      (r) =>
        r.from_country === p.from &&
        r.to_country === p.to &&
        r.pet_type.toLowerCase() === "dog"
    );
    return { ...p, catSlug: cat?.slug, dogSlug: dog?.slug };
  });

  return (
    <main className="mx-auto max-w-5xl px-4 py-10">
      <section className="rounded-2xl border bg-white p-6 shadow-sm">
        <HeroSearch
          fromCountries={fromCountries}
          toCountries={toCountries}
          petTypes={petTypes}
        />
      </section>

      <section className="mt-10">
        <h2 className="text-xl font-semibold tracking-tight">
          Popular routes
        </h2>
        <p className="mt-1 text-sm text-gray-600">
          Jump to common import guides.
        </p>

        <div className="mt-4 grid gap-4 sm:grid-cols-2">
          {popular.map((p) => (
            <RouteCard
              key={`${p.from}-${p.to}`}
              fromCountry={p.from}
              toCountry={p.to}
              catSlug={p.catSlug}
              dogSlug={p.dogSlug}
            />
          ))}
        </div>
      </section>

      <footer className="mt-12 border-t pt-6 text-sm text-gray-500">
        <p>
          PetEntryGuide is a structured knowledge base. Always verify official
          government sources and airline rules before travel.
        </p>
      </footer>
    </main>
  );
}
