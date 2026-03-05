import Link from "next/link";

export const metadata = {
  title: "Cost to Bring a Cat to the USA (Budget Guide)",
  description: "Typical cost buckets: microchip, vaccines, certificate/endorsement, airline fees, and optional services.",
  alternates: { canonical: "https://petentryguide.com/cost-to-bring-cat-to-usa" },
};

export default function Page() {
  return (
    <main className="mx-auto max-w-3xl px-4 py-10">
      <nav className="text-sm text-gray-600">
        <Link className="hover:underline" href="/">Home</Link>
        <span className="mx-2">›</span>
        <span>cost to bring cat to usa</span>
      </nav>

      <header className="mt-4">
        <h1 className="text-2xl font-semibold tracking-tight">
          Cost to Bring a Cat to the USA (Budget Guide)
        </h1>
        <p className="mt-2 text-gray-700">
          Typical cost buckets: microchip, vaccines, certificate/endorsement, airline fees, and optional services.
        </p>
      </header>

      <section className="mt-8">
        <h2 className="text-lg font-semibold">Explanation</h2>
        <p className="mt-2 text-gray-800">
          Costs vary widely by route, airline, and whether you use a pet shipper. This guide breaks down the common line items so you can create a realistic budget.
        </p>
      </section>

      <section className="mt-8">
        <h2 className="text-lg font-semibold">When required</h2>
        <ul className="mt-2 list-disc space-y-2 pl-5 text-gray-800">
          <li>Budgeting a relocation or long-distance travel with a cat</li><li>Comparing cabin travel vs cargo vs pet courier</li>
        </ul>
      </section>

      <section className="mt-8">
        <h2 className="text-lg font-semibold">Common mistakes</h2>
        <ul className="mt-2 list-disc space-y-2 pl-5 text-gray-800">
          <li>Underestimating endorsement fees, re-check visits, or last-minute airline upgrades</li><li>Not budgeting for crate + absorbent pads + travel accessories</li>
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
            <li key="japan-to-usa-cat">
              <Link className="hover:underline" href="/japan-to-usa-cat">
                japan to usa cat
              </Link>
            </li>
            <li key="uk-to-usa-cat">
              <Link className="hover:underline" href="/uk-to-usa-cat">
                uk to usa cat
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
