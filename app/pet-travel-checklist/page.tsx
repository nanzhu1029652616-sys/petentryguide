import Link from "next/link";

export const metadata = {
  title: "Pet Travel Checklist (International): Documents, Crate, Airline, Timeline",
  description: "A step-by-step checklist to reduce last-minute failures when traveling internationally with pets.",
  alternates: { canonical: "https://petentryguide.com/pet-travel-checklist" },
};

export default function Page() {
  return (
    <main className="mx-auto max-w-3xl px-4 py-10">
      <nav className="text-sm text-gray-600">
        <Link className="hover:underline" href="/">Home</Link>
        <span className="mx-2">›</span>
        <span>pet travel checklist</span>
      </nav>

      <header className="mt-4">
        <h1 className="text-2xl font-semibold tracking-tight">
          Pet Travel Checklist (International): Documents, Crate, Airline, Timeline
        </h1>
        <p className="mt-2 text-gray-700">
          A step-by-step checklist to reduce last-minute failures when traveling internationally with pets.
        </p>
      </header>

      <section className="mt-8">
        <h2 className="text-lg font-semibold">Explanation</h2>
        <p className="mt-2 text-gray-800">
          International pet travel is a project: documents, vaccines, microchip, airline policies, crate sizing, and arrival rules. Use this checklist to plan backwards from your travel date.
        </p>
      </section>

      <section className="mt-8">
        <h2 className="text-lg font-semibold">When required</h2>
        <ul className="mt-2 list-disc space-y-2 pl-5 text-gray-800">
          <li>Any international trip with a cat or dog</li><li>Relocations, long-term moves, or multi-country itineraries</li>
        </ul>
      </section>

      <section className="mt-8">
        <h2 className="text-lg font-semibold">Common mistakes</h2>
        <ul className="mt-2 list-disc space-y-2 pl-5 text-gray-800">
          <li>Buying the wrong crate size or missing airline crate rules</li><li>Not keeping printed copies of certificates and forms</li><li>Ignoring transit-country requirements</li>
        </ul>
      </section>

      <section className="mt-8 rounded-2xl border bg-white p-5 shadow-sm">
        <h2 className="text-lg font-semibold">Related guides</h2>
        <ul className="mt-3 list-disc space-y-2 pl-5 text-gray-800">
            <li key="china-to-usa-cat">
              <Link className="hover:underline" href="/china-to-usa-cat">
                china to usa cat
              </Link>
            </li>
            <li key="china-to-usa-dog">
              <Link className="hover:underline" href="/china-to-usa-dog">
                china to usa dog
              </Link>
            </li>
            <li key="japan-to-usa-cat">
              <Link className="hover:underline" href="/japan-to-usa-cat">
                japan to usa cat
              </Link>
            </li>
            <li key="uk-to-usa-dog">
              <Link className="hover:underline" href="/uk-to-usa-dog">
                uk to usa dog
              </Link>
            </li>
        </ul>
      </section>

      <footer className="mt-10 border-t pt-6 text-sm text-gray-500">
        <p>
          Always confirm with official government sources and your airline before travel.
        </p>
      </footer>
    </main>
  );
}
