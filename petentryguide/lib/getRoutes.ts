import fs from 'fs';
import path from 'path';

export interface RouteGuide {
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
}

const routesDir = path.join(process.cwd(), 'data', 'routes');

export function getAllRoutes(): RouteGuide[] {
  const files = fs.readdirSync(routesDir).filter(f => f.endsWith('.json'));
  return files.map(file => {
    const content = fs.readFileSync(path.join(routesDir, file), 'utf-8');
    return JSON.parse(content) as RouteGuide;
  });
}

export function getRouteBySlug(slug: string): RouteGuide | null {
  const filePath = path.join(routesDir, `${slug}.json`);
  if (!fs.existsSync(filePath)) return null;
  const content = fs.readFileSync(filePath, 'utf-8');
  return JSON.parse(content) as RouteGuide;
}

export function getAllSlugs(): string[] {
  return fs.readdirSync(routesDir)
    .filter(f => f.endsWith('.json'))
    .map(f => f.replace('.json', ''));
}

export function getUniqueCountries(): string[] {
  const routes = getAllRoutes();
  const fromSet = new Set(routes.map(r => r.from_country));
  const toSet   = new Set(routes.map(r => r.to_country));
  return Array.from(new Set([...fromSet, ...toSet])).sort();
}

export function getFromCountries(): string[] {
  const routes = getAllRoutes();
  return Array.from(new Set(routes.map(r => r.from_country))).sort();
}

export function getToCountries(): string[] {
  const routes = getAllRoutes();
  return Array.from(new Set(routes.map(r => r.to_country))).sort();
}
