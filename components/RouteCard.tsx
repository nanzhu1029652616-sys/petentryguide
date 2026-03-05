import Link from "next/link";

export default function RouteCard({
  fromCountry,
  toCountry,
  catSlug,
  dogSlug,
}: {
  fromCountry: string;
  toCountry: string;
  catSlug?: string;
  dogSlug?: string;
}) {
  return (
    <div className="rounded-2xl border bg-white p-5 shadow-sm">
      <div className="flex items-baseline justify-between gap-3">
        <div>
          <div className="text-sm text-gray-500">Route</div>
          <div className="mt-1 text-lg font-semibold tracking-tight">
            {fromCountry} → {toCountry}
          </div>
        </div>
      </div>

      <div className="mt-4 flex flex-wrap gap-2">
        {catSlug ? (
          <Link
            className="rounded-full border px-3 py-1 text-sm hover:bg-gray-50"
            href={`/${catSlug}`}
          >
            Cat guide
          </Link>
        ) : (
          <span className="rounded-full border px-3 py-1 text-sm text-gray-400">
            Cat guide
          </span>
        )}

        {dogSlug ? (
          <Link
            className="rounded-full border px-3 py-1 text-sm hover:bg-gray-50"
            href={`/${dogSlug}`}
          >
            Dog guide
          </Link>
        ) : (
          <span className="rounded-full border px-3 py-1 text-sm text-gray-400">
            Dog guide
          </span>
        )}
      </div>
    </div>
  );
}
