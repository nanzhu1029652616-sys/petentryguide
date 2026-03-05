import Link from "next/link";

export const metadata = {
  title: "USDA-Accredited Vet: When You Need One and What They Do",
  description: "How USDA-accredited veterinarians support export certificates and official endorsements.",
  alternates: { canonical: "https://petentryguide.com/usda-accredited-vet" },
};

export default function Page() {
  return (
    <main className="mx-auto max-w-3xl px-4 py-10">
      <nav className="text-sm text-gray-600">
        <Link className="hover:underline" href="/">Home</Link>
        <span className="mx-2">›</span>
        <span>usda accredited vet</span>
      </nav>

      <header className="mt-4">
        <h1 className="text-2xl font-semibold tracking-tight">
          USDA-Accredited Vet: When You Need One and What They Do
        </h1>
        <p className="mt-2 text-gray-700">
          How USDA-accredited veterinarians support export certificates and official endorsements.
        </p>
      </header>

      <section className="mt-8">
        <h2 className="text-lg font-semibold">Explanation</h2>
        <p className="mt-2 text-gray-800">
          For many international pet moves, health certificates must be completed by qualified veterinarians and sometimes endorsed by official authorities. In the US context, a USDA-accredited vet can be required to issue documents that can be endorsed for international travel.
        </p>
      </section>

      <section className="mt-8">
        <h2 className="text-lg font-semibold">When required</h2>
        <ul className="mt-2 list-disc space-y-2 pl-5 text-gray-800">
          <li>When your destination requires an endorsed health certificate</li><li>When official export paperwork must be issued by an accredited provider</li><li>When you need government/authority endorsement workflows</li>
        </ul>
      </section>

      <section className="mt-8">
        <h2 className="text-lg font-semibold">Common mistakes</h2>
        <ul className="mt-2 list-disc space-y-2 pl-5 text-gray-800">
          <li>Booking an appointment too late (endorsement timelines can be tight)</li><li>Not confirming destination-specific certificate versions</li><li>Incomplete owner or pet identification fields</li>
        </ul>
      </section>

      <section className="mt-8 rounded-2xl border bg-white p-5 shadow-sm">
        <h2 className="text-lg font-semibold">Related guides</h2>
        <ul className="mt-3 list-disc space-y-2 pl-5 text-gray-800">
            <li key="usa-to-uk-dog">
              <Link className="hover:underline" href="/usa-to-uk-dog">
                usa to uk dog
              </Link>
            </li>
            <li key="usa-to-japan-cat">
              <Link className="hover:underline" href="/usa-to-japan-cat">
                usa to japan cat
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
