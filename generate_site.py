#!/usr/bin/env python3
"""
generate_site.py

Generates a fully-static, SEO-friendly Next.js (App Router) site skeleton for:
  PetEntryGuide (petentryguide.com)

What it creates/overwrites (safe, deterministic):
- /app
  - page.tsx
  - /[slug]/page.tsx
  - static content pages at root:
      /rabies-vaccine-requirements
      /cdc-dog-import-rule
      /usda-accredited-vet
      /pet-travel-checklist
      /cost-to-bring-cat-to-usa
      /pet-cargo-travel-guide
- /components
  - HeroSearch.tsx
  - RouteCard.tsx
  - SummaryGrid.tsx
  - ProcessSteps.tsx
  - DocumentList.tsx
- /lib
  - getRoutes.ts
- /data/routes/*.json  (>= 20 example route pages)
- /public/sitemap.xml

Usage:
  python3 generate_site.py
  python3 generate_site.py --force    # overwrite files if they already exist
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple


BASE_URL = "https://petentryguide.com"


# -------------------------
# Utilities
# -------------------------

def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_text(path: Path, content: str, *, force: bool) -> None:
    ensure_dir(path.parent)
    if path.exists() and not force:
        return
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, obj: Dict, *, force: bool) -> None:
    ensure_dir(path.parent)
    if path.exists() and not force:
        return
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def slugify_country(country: str) -> str:
    # Minimal slug for example data (you can expand later)
    return country.strip().lower().replace(" ", "-")


def make_route_slug(from_country: str, to_country: str, pet_type: str) -> str:
    return f"{slugify_country(from_country)}-to-{slugify_country(to_country)}-{pet_type.strip().lower()}"


# -------------------------
# Example content sets (V1)
# -------------------------

@dataclass(frozen=True)
class ContentPage:
    slug: str  # root-level path segment, e.g. "rabies-vaccine-requirements"
    title: str
    summary: str
    explanation: str
    when_required: List[str]
    common_mistakes: List[str]
    related_guides: List[str]  # route slugs, e.g. "china-to-usa-cat"


RULE_PAGES: List[ContentPage] = [
    ContentPage(
        slug="rabies-vaccine-requirements",
        title="Rabies Vaccine Requirements for International Pet Travel",
        summary="What rabies vaccination rules typically require, what proof you need, and common pitfalls.",
        explanation=(
            "Many countries require a valid rabies vaccination for dogs and cats. Rules vary by destination, "
            "including vaccine timing windows, accepted vaccine types, and documentation format. "
            "Always follow the destination country's official import guidance and your airline's requirements."
        ),
        when_required=[
            "Most dog and cat imports into rabies-free or controlled countries",
            "When transiting through countries that require proof for entry",
            "When airlines request vaccination proof to allow boarding",
        ],
        common_mistakes=[
            "Vaccination given too close to departure (outside the required waiting window)",
            "Certificate missing microchip number or date details",
            "Using non-accepted documentation formats or missing official endorsements",
        ],
        related_guides=[
            "china-to-usa-cat",
            "china-to-usa-dog",
            "uk-to-usa-dog",
            "japan-to-usa-cat",
        ],
    ),
    ContentPage(
        slug="cdc-dog-import-rule",
        title="CDC Dog Import Rule (USA): What It Means for Travelers",
        summary="A practical explanation of CDC requirements that can affect importing dogs into the United States.",
        explanation=(
            "The CDC may require specific documentation or eligibility conditions for importing dogs into the USA, "
            "especially related to rabies risk and vaccination history. Requirements can change—verify the latest "
            "CDC guidance before travel and keep copies of all documents."
        ),
        when_required=[
            "Bringing a dog into the United States (as a personal pet or relocation)",
            "Traveling from countries with higher rabies risk classifications",
            "When the dog’s vaccination or microchip history needs to be verified",
        ],
        common_mistakes=[
            "Assuming airline approval equals border entry approval",
            "Missing required forms or incorrect information on forms",
            "Not planning for additional lead time if pre-approvals are needed",
        ],
        related_guides=[
            "china-to-usa-dog",
            "australia-to-usa-dog",
            "uk-to-usa-dog",
        ],
    ),
    ContentPage(
        slug="usda-accredited-vet",
        title="USDA-Accredited Vet: When You Need One and What They Do",
        summary="How USDA-accredited veterinarians support export certificates and official endorsements.",
        explanation=(
            "For many international pet moves, health certificates must be completed by qualified veterinarians and "
            "sometimes endorsed by official authorities. In the US context, a USDA-accredited vet can be required "
            "to issue documents that can be endorsed for international travel."
        ),
        when_required=[
            "When your destination requires an endorsed health certificate",
            "When official export paperwork must be issued by an accredited provider",
            "When you need government/authority endorsement workflows",
        ],
        common_mistakes=[
            "Booking an appointment too late (endorsement timelines can be tight)",
            "Not confirming destination-specific certificate versions",
            "Incomplete owner or pet identification fields",
        ],
        related_guides=[
            "usa-to-uk-dog",
            "usa-to-japan-cat",
        ],
    ),
]

PRACTICAL_GUIDES: List[ContentPage] = [
    ContentPage(
        slug="pet-travel-checklist",
        title="Pet Travel Checklist (International): Documents, Crate, Airline, Timeline",
        summary="A step-by-step checklist to reduce last-minute failures when traveling internationally with pets.",
        explanation=(
            "International pet travel is a project: documents, vaccines, microchip, airline policies, crate sizing, "
            "and arrival rules. Use this checklist to plan backwards from your travel date."
        ),
        when_required=[
            "Any international trip with a cat or dog",
            "Relocations, long-term moves, or multi-country itineraries",
        ],
        common_mistakes=[
            "Buying the wrong crate size or missing airline crate rules",
            "Not keeping printed copies of certificates and forms",
            "Ignoring transit-country requirements",
        ],
        related_guides=[
            "china-to-usa-cat",
            "china-to-usa-dog",
            "japan-to-usa-cat",
            "uk-to-usa-dog",
        ],
    ),
    ContentPage(
        slug="cost-to-bring-cat-to-usa",
        title="Cost to Bring a Cat to the USA (Budget Guide)",
        summary="Typical cost buckets: microchip, vaccines, certificate/endorsement, airline fees, and optional services.",
        explanation=(
            "Costs vary widely by route, airline, and whether you use a pet shipper. This guide breaks down the "
            "common line items so you can create a realistic budget."
        ),
        when_required=[
            "Budgeting a relocation or long-distance travel with a cat",
            "Comparing cabin travel vs cargo vs pet courier",
        ],
        common_mistakes=[
            "Underestimating endorsement fees, re-check visits, or last-minute airline upgrades",
            "Not budgeting for crate + absorbent pads + travel accessories",
        ],
        related_guides=[
            "china-to-usa-cat",
            "japan-to-usa-cat",
            "uk-to-usa-cat",
        ],
    ),
    ContentPage(
        slug="pet-cargo-travel-guide",
        title="Pet Cargo Travel Guide: Safety, Airline Rules, and Preparation",
        summary="How cargo transport works, how to choose an airline, and how to reduce risks.",
        explanation=(
            "Cargo rules differ by airline and season. Understanding temperature embargoes, crate ventilation, "
            "and check-in procedures helps reduce travel risk."
        ),
        when_required=[
            "When cabin travel is not possible due to pet size or airline policy",
            "When flying long-haul routes with limited cabin availability",
        ],
        common_mistakes=[
            "Flying during embargo seasons without backups",
            "Using crates that fail airline inspection",
            "Not practicing crate time before travel day",
        ],
        related_guides=[
            "china-to-usa-dog",
            "australia-to-usa-dog",
            "uk-to-usa-dog",
        ],
    ),
]


def build_example_routes() -> List[Dict]:
    """
    Build >= 20 route guides for V1.
    You can replace/extend these later; the site reads from /data/routes/*.json.
    """
    from_countries = ["China", "Japan", "UK", "Australia", "Canada", "USA"]
    to_countries = ["USA", "Canada", "UK", "Japan"]
    pet_types = ["cat", "dog"]

    # Curated subset first (explicitly asked examples)
    curated_pairs: List[Tuple[str, str]] = [
        ("China", "USA"),
        ("Japan", "USA"),
        ("UK", "USA"),
        ("Australia", "USA"),
        ("China", "Canada"),
        ("USA", "UK"),
        ("USA", "Japan"),
    ]

    routes: List[Dict] = []

    def make_route(from_c: str, to_c: str, pet: str) -> Dict:
        slug = make_route_slug(from_c, to_c, pet)
        pet_title = pet.capitalize()
        return {
            "from_country": from_c,
            "to_country": to_c,
            "pet_type": pet,
            "slug": slug,
            "title": f"Bring a {pet_title} from {from_c} to the {to_c} (2026 Guide)",
            "summary": f"Requirements for importing a {pet} from {from_c} to {to_c}.",
            "min_age": "6 months",
            "microchip": "ISO 11784/85 required",
            "rabies_vaccine": "Required",
            "quarantine": "No",
            "process_steps": [
                "Microchip the pet",
                "Administer rabies vaccination",
                "Obtain export health certificate",
                "Complete required import form(s)",
                "Travel with an approved airline",
            ],
            "required_documents": [
                "Export Health Certificate",
                "Rabies Vaccination Certificate",
                "Import Form (if required)",
            ],
            "vaccines": [
                "Rabies Vaccine",
            ],
            "travel_methods": [
                "Cabin travel",
                "Cargo transport",
            ],
            "tips": [
                "Health certificates may need endorsement by official government veterinarians.",
                "Check airline seasonal cargo embargo rules before booking.",
            ],
        }

    # Add curated (2 pets each)
    for fr, to in curated_pairs:
        for pet in pet_types:
            routes.append(make_route(fr, to, pet))

    # Add more combinations until we have >= 20, avoiding from==to
    for fr in from_countries:
        for to in to_countries:
            if fr == to:
                continue
            for pet in pet_types:
                slug = make_route_slug(fr, to, pet)
                if any(r["slug"] == slug for r in routes):
                    continue
                routes.append(make_route(fr, to, pet))
                if len(routes) >= 22:
                    break
            if len(routes) >= 22:
                break
        if len(routes) >= 22:
            break

    return routes


# -------------------------
# File templates
# -------------------------

APP_HOME_PAGE_TSX = r"""import { getAllRoutes } from "@/lib/getRoutes";
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
"""

APP_ROUTE_PAGE_TSX = r"""import { notFound } from "next/navigation";
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
"""

COMP_HEROSEARCH_TSX = r""""use client";

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
"""

COMP_ROUTECARD_TSX = r"""import Link from "next/link";

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
"""

COMP_SUMMARYGRID_TSX = r"""export default function SummaryGrid({
  items,
}: {
  items: Array<{ label: string; value: string }>;
}) {
  return (
    <div className="grid gap-3 sm:grid-cols-2">
      {items.map((it) => (
        <div
          key={it.label}
          className="rounded-2xl border bg-white p-4 shadow-sm"
        >
          <div className="text-xs font-medium uppercase tracking-wide text-gray-500">
            {it.label}
          </div>
          <div className="mt-2 text-sm text-gray-900">{it.value}</div>
        </div>
      ))}
    </div>
  );
}
"""

COMP_PROCESSSTEPS_TSX = r"""export default function ProcessSteps({ steps }: { steps: string[] }) {
  return (
    <ol className="space-y-3">
      {steps.map((s, idx) => (
        <li key={idx} className="rounded-2xl border bg-white p-4 shadow-sm">
          <div className="text-sm font-semibold">
            Step {idx + 1} <span className="font-normal text-gray-500">–</span>{" "}
            <span className="font-normal">{s}</span>
          </div>
        </li>
      ))}
    </ol>
  );
}
"""

COMP_DOCUMENTLIST_TSX = r"""export default function DocumentList({ items }: { items: string[] }) {
  return (
    <ul className="list-disc space-y-2 pl-5 text-gray-800">
      {items.map((d, idx) => (
        <li key={idx}>{d}</li>
      ))}
    </ul>
  );
}
"""

LIB_GETROUTES_TS = r"""import fs from "fs";
import path from "path";

export type RouteGuide = {
  from_country: string;
  to_country: string;
  pet_type: string;
  slug: string;
  title: string;
  summary: string;

  min_age: string;
  microchip: string;
  rabies_vaccine: string;
  quarantine: string;

  process_steps: string[];
  required_documents: string[];
  vaccines: string[];
  travel_methods: string[];
  tips: string[];
};

const ROUTES_DIR = path.join(process.cwd(), "data", "routes");

export function getAllRoutes(): RouteGuide[] {
  const files = fs
    .readdirSync(ROUTES_DIR)
    .filter((f) => f.toLowerCase().endsWith(".json"));

  const routes = files.map((file) => {
    const full = path.join(ROUTES_DIR, file);
    const raw = fs.readFileSync(full, "utf-8");
    return JSON.parse(raw) as RouteGuide;
  });

  // stable ordering (helps deterministic builds)
  routes.sort((a, b) => a.slug.localeCompare(b.slug));
  return routes;
}

export function getAllRouteSlugs(): string[] {
  return getAllRoutes().map((r) => r.slug);
}

export function getRouteBySlug(slug: string): RouteGuide | null {
  const full = path.join(ROUTES_DIR, `${slug}.json`);
  if (!fs.existsSync(full)) return null;
  const raw = fs.readFileSync(full, "utf-8");
  return JSON.parse(raw) as RouteGuide;
}
"""

def content_page_tsx(page: ContentPage) -> str:
    # Root-level page in /app/{slug}/page.tsx (SSG by default in App Router)
    # Includes canonical, title, description; and "Related guides" links.
    related_links = "\n".join(
        [
            f"""            <li key="{slug}">
              <Link className="hover:underline" href="/{slug}">
                {slug.replace("-", " ")}
              </Link>
            </li>"""
            for slug in page.related_guides
        ]
    ) or """            <li className="text-gray-500">No related guides yet.</li>"""

    return f"""import Link from "next/link";

export const metadata = {{
  title: "{page.title}",
  description: "{page.summary}",
  alternates: {{ canonical: "{BASE_URL}/{page.slug}" }},
}};

export default function Page() {{
  return (
    <main className="mx-auto max-w-3xl px-4 py-10">
      <nav className="text-sm text-gray-600">
        <Link className="hover:underline" href="/">Home</Link>
        <span className="mx-2">›</span>
        <span>{page.slug.replace("-", " ")}</span>
      </nav>

      <header className="mt-4">
        <h1 className="text-2xl font-semibold tracking-tight">
          {page.title}
        </h1>
        <p className="mt-2 text-gray-700">
          {page.summary}
        </p>
      </header>

      <section className="mt-8">
        <h2 className="text-lg font-semibold">Explanation</h2>
        <p className="mt-2 text-gray-800">
          {page.explanation}
        </p>
      </section>

      <section className="mt-8">
        <h2 className="text-lg font-semibold">When required</h2>
        <ul className="mt-2 list-disc space-y-2 pl-5 text-gray-800">
          {''.join([f"<li>{x}</li>" for x in page.when_required])}
        </ul>
      </section>

      <section className="mt-8">
        <h2 className="text-lg font-semibold">Common mistakes</h2>
        <ul className="mt-2 list-disc space-y-2 pl-5 text-gray-800">
          {''.join([f"<li>{x}</li>" for x in page.common_mistakes])}
        </ul>
      </section>

      <section className="mt-8 rounded-2xl border bg-white p-5 shadow-sm">
        <h2 className="text-lg font-semibold">Related guides</h2>
        <ul className="mt-3 list-disc space-y-2 pl-5 text-gray-800">
{related_links}
        </ul>
      </section>

      <footer className="mt-10 border-t pt-6 text-sm text-gray-500">
        <p>
          Always confirm with official government sources and your airline before travel.
        </p>
      </footer>
    </main>
  );
}}
"""


def build_sitemap_xml(route_slugs: List[str], content_slugs: List[str]) -> str:
    # Simple static sitemap generator (no lastmod to keep it stable)
    urls = ["/"] + [f"/{s}" for s in route_slugs] + [f"/{s}" for s in content_slugs]
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for u in urls:
        lines.append("  <url>")
        lines.append(f"    <loc>{BASE_URL}{u}</loc>")
        lines.append("  </url>")
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


# -------------------------
# Main generation
# -------------------------

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true", help="overwrite existing files")
    args = parser.parse_args()
    force = bool(args.force)

    root = Path.cwd()

    # Directories
    app_dir = root / "app"
    components_dir = root / "components"
    lib_dir = root / "lib"
    data_routes_dir = root / "data" / "routes"
    public_dir = root / "public"

    ensure_dir(app_dir)
    ensure_dir(components_dir)
    ensure_dir(lib_dir)
    ensure_dir(data_routes_dir)
    ensure_dir(public_dir)

    # Generate route JSON files
    routes = build_example_routes()
    for r in routes:
        write_json(data_routes_dir / f"{r['slug']}.json", r, force=force)

    # Core app pages
    write_text(app_dir / "page.tsx", APP_HOME_PAGE_TSX, force=force)
    write_text(app_dir / "[slug]" / "page.tsx", APP_ROUTE_PAGE_TSX, force=force)

    # Components
    write_text(components_dir / "HeroSearch.tsx", COMP_HEROSEARCH_TSX, force=force)
    write_text(components_dir / "RouteCard.tsx", COMP_ROUTECARD_TSX, force=force)
    write_text(components_dir / "SummaryGrid.tsx", COMP_SUMMARYGRID_TSX, force=force)
    write_text(components_dir / "ProcessSteps.tsx", COMP_PROCESSSTEPS_TSX, force=force)
    write_text(components_dir / "DocumentList.tsx", COMP_DOCUMENTLIST_TSX, force=force)

    # Lib
    write_text(lib_dir / "getRoutes.ts", LIB_GETROUTES_TS, force=force)

    # Rule + Practical pages as ROOT-LEVEL slugs (so they don't conflict with /[slug] route guides)
    # We generate /app/{slug}/page.tsx for each content page.
    content_pages = RULE_PAGES + PRACTICAL_GUIDES
    for p in content_pages:
        write_text(app_dir / p.slug / "page.tsx", content_page_tsx(p), force=force)

    # Sitemap
    route_slugs = sorted([r["slug"] for r in routes])
    content_slugs = sorted([p.slug for p in content_pages])
    sitemap = build_sitemap_xml(route_slugs, content_slugs)
    write_text(public_dir / "sitemap.xml", sitemap, force=force)

    print("✅ PetEntryGuide site scaffold generated.")
    print(f"   Routes: {len(route_slugs)} JSON files in data/routes/")
    print(f"   Content pages: {len(content_slugs)} root-level pages in app/*/page.tsx")
    print("   Sitemap: public/sitemap.xml")
    print("")
    print("Next steps (manual):")
    print("  - Ensure TailwindCSS is installed/configured in your Next.js project.")
    print("  - Run: npm run build && npm run start (or your deployment pipeline).")


if __name__ == "__main__":
    main()
