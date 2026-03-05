import Link from "next/link";

export const metadata = {
  title: "Pet Cargo Travel Guide: Safety, Airline Rules, and Preparation",
  description: "How cargo transport works, how to choose an airline, and how to reduce risks.",
  alternates: { canonical: "https://petentryguide.com/pet-cargo-travel-guide" },
};

export default function Page() {
  return (
    <main className="mx-auto max-w-3xl px-4 py-10">
      <nav className="text-sm text-gray-600">
        <Link className="hover:underline" href="/">Home</Link>
        <span className="mx-2">›</span>
        <span>pet cargo travel guide</span>
      </nav>

      <header className="mt-4">
        <h1 className="text-2xl font-semibold tracking-tight">
          Pet Cargo Travel Guide: Safety, Airline Rules, and Preparation
        </h1>
        <p className="mt-2 text-gray-700">
          How cargo transport works, how to choose an airline, and how to reduce risks.
        </p>
      </header>

      <section className="mt-8">
        <h2 className="text-lg font-semibold">Explanation</h2>
        <p className="mt-2 text-gray-800">
          Cargo rules differ by airline and season. Understanding temperature embargoes, crate ventilation, and check-in procedures helps reduce travel risk.
        </p>
      </section>

      <section className="mt-8">
        <h2 className="text-lg font-semibold">When required</h2>
        <ul className="mt-2 list-disc space-y-2 pl-5 text-gray-800">
          <li>When cabin travel is not possible due to pet size or airline policy</li><li>When flying long-haul routes with limited cabin availability</li>
        </ul>
      </section>

      <section className="mt-8">
        <h2 className="text-lg font-semibold">Common mistakes</h2>
        <ul className="mt-2 list-disc space-y-2 pl-5 text-gray-800">
          <li>Flying during embargo seasons without backups</li><li>Using crates that fail airline inspection</li><li>Not practicing crate time before travel day</li>
        </ul>
      </section>

      <section className="mt-8 rounded-2xl border bg-white p-5 shadow-sm">
        <h2 className="text-lg font-semibold">Related guides</h2>
        <ul className="mt-3 list-disc space-y-2 pl-5 text-gray-800">
            <li key="china-to-usa-dog">
              <Link className="hover:underline" href="/china-to-usa-dog">
                china to usa dog
              </Link>
            </li>
            <li key="australia-to-usa-dog">
              <Link className="hover:underline" href="/australia-to-usa-dog">
                australia to usa dog
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
