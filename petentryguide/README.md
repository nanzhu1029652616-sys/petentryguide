# PetEntryGuide

Static Next.js site for international pet import requirements.

## Setup

```bash
npm install
npm run dev       # development
npm run build     # static export → /out
```

## Structure

```
/app              – Next.js App Router pages
/components       – Reusable UI components
/data/routes      – JSON data for 23 route guides
/lib              – getRoutes.ts data helpers
```

## Routes Generated

- /china-to-usa-cat
- /china-to-usa-dog
- /japan-to-usa-cat
- /japan-to-usa-dog
- /uk-to-usa-cat
- /uk-to-usa-dog
- /australia-to-usa-cat
- /australia-to-usa-dog
- /canada-to-usa-cat
- /canada-to-usa-dog
- /germany-to-usa-cat
- /germany-to-usa-dog
- /france-to-usa-cat
- /france-to-usa-dog
- /india-to-usa-cat
- /india-to-usa-dog
- /south-korea-to-usa-cat
- /south-korea-to-usa-dog
- /mexico-to-usa-cat
- /mexico-to-usa-dog
- /brazil-to-usa-dog
- /new-zealand-to-usa-cat
- /singapore-to-usa-dog

## Static Pages

- /rabies-vaccine-requirements
- /cdc-dog-import-rule
- /usda-accredited-vet
- /pet-travel-checklist
- /cost-to-bring-cat-to-usa
- /pet-cargo-travel-guide

## Tech Stack

- Next.js 14 (App Router)
- TypeScript
- TailwindCSS
- Static Site Generation (SSG)
