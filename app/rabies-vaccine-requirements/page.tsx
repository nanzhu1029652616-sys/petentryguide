import Link from "next/link";

export const metadata = {
  title: "Rabies Vaccine Requirements for International Pet Travel",
  description: "What rabies vaccination rules typically require, what proof you need, and common pitfalls.",
  alternates: { canonical: "https://petentryguide.com/rabies-vaccine-requirements" },
};

export default function Page() {
  return (
    <main className="mx-auto max-w-3xl px-4 py-10">
      <nav className="text-sm text-gray-600">
        <Link className="hover:underline" href="/">Home</Link>
        <span className="mx-2">›</span>
        <span>rabies vaccine requirements</span>
      </nav>

      <header className="mt-4">
        <h1 className="text-2xl font-semibold tracking-tight">
          Rabies Vaccine Requirements for International Pet Travel
        </h1>
        <p className="mt-2 text-gray-700">
          What rabies vaccination rules typically require, what proof you need, and common pitfalls.
        </p>
      </header>

      <section className="mt-8">
        <h2 className="text-lg font-semibold">Explanation</h2>
        <p className="mt-2 text-gray-800">
          Many countries require a valid rabies vaccination for dogs and cats. Rules vary by destination, including vaccine timing windows, accepted vaccine types, and documentation format. Always follow the destination country's official import guidance and your airline's requirements.
        </p>
      </section>

      <section className="mt-8">
        <h2 className="text-lg font-semibold">When required</h2>
        <ul className="mt-2 list-disc space-y-2 pl-5 text-gray-800">
          <li>Most dog and cat imports into rabies-free or controlled countries</li><li>When transiting through countries that require proof for entry</li><li>When airlines request vaccination proof to allow boarding</li>
        </ul>
      </section>

      <section className="mt-8">
        <h2 className="text-lg font-semibold">Common mistakes</h2>
        <ul className="mt-2 list-disc space-y-2 pl-5 text-gray-800">
          <li>Vaccination given too close to departure (outside the required waiting window)</li><li>Certificate missing microchip number or date details</li><li>Using non-accepted documentation formats or missing official endorsements</li>
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
            <li key="uk-to-usa-dog">
              <Link className="hover:underline" href="/uk-to-usa-dog">
                uk to usa dog
              </Link>
            </li>
            <li key="japan-to-usa-cat">
              <Link className="hover:underline" href="/japan-to-usa-cat">
                japan to usa cat
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
