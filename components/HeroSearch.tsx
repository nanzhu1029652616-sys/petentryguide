"use client";

import { useMemo, useState } from "react";
import { useRouter } from "next/navigation";

type Props = {
  fromCountries: string[];
  toCountries: string[];
  petTypes: string[];
};

function toSlugPart(v: string) {
  return v.trim().toLowerCase().replace(/\s+/g, "-");
}

export default function HeroSearch({ fromCountries, toCountries, petTypes }: Props) {
  const router = useRouter();

  const [from, setFrom] = useState(fromCountries[0] ?? "");
  const [to, setTo] = useState(toCountries[0] ?? "");
  const [pet, setPet] = useState(petTypes[0] ?? "cat");

  const canSearch = useMemo(() => {
    return Boolean(from && to && pet) && from !== to;
  }, [from, to, pet]);

  const onSearch = () => {
    if (!canSearch) return;
    const slug = `${toSlugPart(from)}-to-${toSlugPart(to)}-${toSlugPart(pet)}`;
    router.push(`/${slug}`);
  };

  return (
    <div>
      <div className="flex flex-col gap-2">
        <h1 className="text-2xl font-semibold tracking-tight">
          Find Pet Import Requirements Worldwide
        </h1>
        <p className="text-gray-700">
          Search official import rules for traveling internationally with pets.
        </p>
      </div>

      <div className="mt-6 grid gap-3 md:grid-cols-4">
        <label className="flex flex-col gap-1">
          <span className="text-sm font-medium text-gray-700">From Country</span>
          <select
            className="rounded-xl border bg-white px-3 py-2"
            value={from}
            onChange={(e) => setFrom(e.target.value)}
          >
            {fromCountries.map((c) => (
              <option key={c} value={c}>
                {c}
              </option>
            ))}
          </select>
        </label>

        <label className="flex flex-col gap-1">
          <span className="text-sm font-medium text-gray-700">To Country</span>
          <select
            className="rounded-xl border bg-white px-3 py-2"
            value={to}
            onChange={(e) => setTo(e.target.value)}
          >
            {toCountries.map((c) => (
              <option key={c} value={c}>
                {c}
              </option>
            ))}
          </select>
        </label>

        <label className="flex flex-col gap-1">
          <span className="text-sm font-medium text-gray-700">Pet Type</span>
          <select
            className="rounded-xl border bg-white px-3 py-2 capitalize"
            value={pet}
            onChange={(e) => setPet(e.target.value)}
          >
            {petTypes.map((p) => (
              <option key={p} value={p} className="capitalize">
                {p}
              </option>
            ))}
          </select>
        </label>

        <div className="flex items-end">
          <button
            type="button"
            onClick={onSearch}
            disabled={!canSearch}
            className="w-full rounded-xl border bg-gray-900 px-4 py-2 text-white shadow-sm disabled:cursor-not-allowed disabled:opacity-50"
          >
            Search Requirements
          </button>
        </div>
      </div>

      {!canSearch ? (
        <p className="mt-3 text-sm text-gray-500">
          Select different origin and destination to search.
        </p>
      ) : null}
    </div>
  );
}
