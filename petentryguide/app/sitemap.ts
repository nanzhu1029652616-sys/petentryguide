import { MetadataRoute } from 'next';

const BASE_URL = 'https://petentryguide.com';

const ROUTE_SLUGS = [
    'china-to-usa-cat',
    'china-to-usa-dog',
    'japan-to-usa-cat',
    'japan-to-usa-dog',
    'uk-to-usa-cat',
    'uk-to-usa-dog',
    'australia-to-usa-cat',
    'australia-to-usa-dog',
    'canada-to-usa-cat',
    'canada-to-usa-dog',
    'germany-to-usa-cat',
    'germany-to-usa-dog',
    'france-to-usa-cat',
    'france-to-usa-dog',
    'india-to-usa-cat',
    'india-to-usa-dog',
    'south-korea-to-usa-cat',
    'south-korea-to-usa-dog',
    'mexico-to-usa-cat',
    'mexico-to-usa-dog',
    'brazil-to-usa-dog',
    'new-zealand-to-usa-cat',
    'singapore-to-usa-dog',
];

const STATIC_PAGES = [
  '/rabies-vaccine-requirements',
  '/cdc-dog-import-rule',
  '/usda-accredited-vet',
  '/pet-travel-checklist',
  '/cost-to-bring-cat-to-usa',
  '/pet-cargo-travel-guide',
];

export default function sitemap(): MetadataRoute.Sitemap {
  const routes = ROUTE_SLUGS.map(slug => ({
    url: `${BASE_URL}/${slug}`,
    lastModified: new Date(),
    changeFrequency: 'monthly' as const,
    priority: 0.8,
  }));

  const staticPages = STATIC_PAGES.map(path => ({
    url: `${BASE_URL}${path}`,
    lastModified: new Date(),
    changeFrequency: 'monthly' as const,
    priority: 0.6,
  }));

  return [
    { url: BASE_URL, lastModified: new Date(), changeFrequency: 'weekly', priority: 1 },
    ...routes,
    ...staticPages,
  ];
}
