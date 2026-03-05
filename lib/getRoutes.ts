import fs from "fs";
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
