import Link from "next/link";

export const metadata = {
  title: "CDC Dog Import Rule (USA): What It Means for Travelers",
  description: "A practical explanation of CDC requirements that can affect importing dogs into the United States.",
  alternates: { canonical: "https://petentryguide.com/cdc-dog-import-rule" },
};

export default function Page() {
  return (
    <main className="mx-auto max-w-3xl px-4 py-10">
      <nav className="text-sm text-gray-600">
        <Link className="hover:underline" href="/">Home</Link>
        <span className="mx-2">›</span>
        <span>cdc dog import rule</span>
      </nav>

      <header className="mt-4">
        <h1 className="text-2xl font-semibold tracking-tight">
          CDC Dog Import Rule (USA): What It Means for Travelers
        </h1>
        <p className="mt-2 text-gray-700">
          A practical explanation of CDC requirements that can affect importing dogs into the United States.
        </p>
      </header>

      <section className="mt-8">
        <h2 className="text-lg font-semibold">Explanation</h2>
        <p className="mt-2 text-gray-800">
          The CDC may require specific documentation or eligibility conditions for importing dogs into the USA, especially related to rabies risk and vaccination history. Requirements can change—verify the latest CDC guidance before travel and keep copies of all documents.
        </p>
      </section>

      <section className="mt-8">
        <h2 className="text-lg font-semibold">When required</h2>
        <ul className="mt-2 list-disc space-y-2 pl-5 text-gray-800">
          <li>Bringing a dog into the United States (as a personal pet or relocation)</li><li>Traveling from countries with higher rabies risk classifications</li><li>When the dog’s vaccination or microchip history needs to be verified</li>
        </ul>
      </section>

      <section className="mt-8">
        <h2 className="text-lg font-semibold">Common mistakes</h2>
        <ul className="mt-2 list-disc space-y-2 pl-5 text-gray-800">
          <li>Assuming airline approval equals border entry approval</li><li>Missing required forms or incorrect information on forms</li><li>Not planning for additional lead time if pre-approvals are needed</li>
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
