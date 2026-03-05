#!/usr/bin/env python3
"""
PetEntryGuide Static Site Generator
Generates a complete Next.js (App Router) + TypeScript + TailwindCSS static site
for international pet import requirements.
"""

import os
import json

BASE_DIR = "petentryguide"

# ─────────────────────────────────────────────
# ROUTE DATA (20+ routes)
# ─────────────────────────────────────────────

ROUTES = [
    {
        "from_country": "China",
        "to_country": "USA",
        "pet_type": "cat",
        "slug": "china-to-usa-cat",
        "title": "Bring a Cat from China to the USA (2026 Guide)",
        "summary": "Requirements for importing a cat from China to the United States.",
        "min_age": "6 months",
        "microchip": "ISO 11784/85 required",
        "rabies_vaccine": "Required",
        "quarantine": "No",
        "process_steps": [
            "Microchip the cat with ISO 11784/85 compliant chip",
            "Administer rabies vaccination (after microchipping)",
            "Obtain Export Health Certificate from accredited vet",
            "Complete CDC import form online",
            "Book airline that accepts pets in cabin or cargo",
            "Arrive at port of entry with all documents ready"
        ],
        "required_documents": [
            "Export Health Certificate (endorsed by GACC)",
            "Rabies Vaccination Certificate",
            "CDC Import Form (dogs only, but recommended)",
            "Microchip Certificate"
        ],
        "vaccines": ["Rabies Vaccine"],
        "travel_methods": ["Cabin travel (under 20 lbs)", "Cargo transport", "Pet courier service"],
        "tips": [
            "Health certificates must be endorsed by government veterinarians.",
            "Book flights at least 2 months in advance during peak seasons.",
            "Check airline-specific pet policies before purchasing tickets."
        ]
    },
    {
        "from_country": "China",
        "to_country": "USA",
        "pet_type": "dog",
        "slug": "china-to-usa-dog",
        "title": "Bring a Dog from China to the USA (2026 Guide)",
        "summary": "CDC and USDA requirements for importing a dog from China to the United States.",
        "min_age": "6 months",
        "microchip": "ISO 11784/85 required",
        "rabies_vaccine": "Required (CDC-approved facility)",
        "quarantine": "Possible (if not vaccinated at CDC-approved facility)",
        "process_steps": [
            "Microchip the dog with ISO 11784/85 chip",
            "Vaccinate at a CDC-approved facility in China",
            "Obtain USDA-endorsed health certificate",
            "Complete CDC Dog Import Form online",
            "Receive CDC Import Code via email",
            "Present all documents at US port of entry"
        ],
        "required_documents": [
            "CDC Dog Import Form (mandatory)",
            "Proof of CDC-approved rabies vaccination",
            "Export Health Certificate (GACC endorsed)",
            "Microchip documentation",
            "Airline health certificate"
        ],
        "vaccines": ["Rabies Vaccine (CDC-approved facility required)", "DHPP recommended"],
        "travel_methods": ["Cargo transport (most common)", "Cabin travel (small breeds)", "Pet relocation service"],
        "tips": [
            "China requires vaccination at CDC-approved facilities; verify the list at cdc.gov.",
            "The CDC Dog Import Form must be submitted before travel.",
            "Allow 4–6 months for the full vaccination and documentation process."
        ]
    },
    {
        "from_country": "Japan",
        "to_country": "USA",
        "pet_type": "cat",
        "slug": "japan-to-usa-cat",
        "title": "Bring a Cat from Japan to the USA (2026 Guide)",
        "summary": "Import requirements for bringing a cat from Japan to the United States.",
        "min_age": "No minimum for cats",
        "microchip": "ISO 11784/85 recommended",
        "rabies_vaccine": "Recommended",
        "quarantine": "No",
        "process_steps": [
            "Microchip the cat (ISO standard recommended)",
            "Obtain rabies vaccination",
            "Get health certificate from licensed Japanese vet",
            "Have health certificate endorsed by MAFF (Japan)",
            "Arrive at US port of entry"
        ],
        "required_documents": [
            "Health Certificate (MAFF endorsed)",
            "Rabies Vaccination Certificate",
            "Microchip Record"
        ],
        "vaccines": ["Rabies Vaccine (recommended)"],
        "travel_methods": ["Cabin travel", "Cargo transport"],
        "tips": [
            "Japan is rabies-free; US entry for cats from Japan is relatively straightforward.",
            "Keep all vaccination records in English or with certified translation."
        ]
    },
    {
        "from_country": "Japan",
        "to_country": "USA",
        "pet_type": "dog",
        "slug": "japan-to-usa-dog",
        "title": "Bring a Dog from Japan to the USA (2026 Guide)",
        "summary": "CDC and USDA requirements for importing a dog from Japan to the United States.",
        "min_age": "6 months",
        "microchip": "ISO 11784/85 required",
        "rabies_vaccine": "Required",
        "quarantine": "No (if fully vaccinated)",
        "process_steps": [
            "Microchip the dog with ISO chip",
            "Administer rabies vaccination after microchipping",
            "Complete CDC Dog Import Form before travel",
            "Obtain health certificate endorsed by MAFF",
            "Present CDC Import Code at US entry"
        ],
        "required_documents": [
            "CDC Dog Import Form",
            "MAFF-endorsed Health Certificate",
            "Rabies Vaccination Certificate",
            "Microchip Certificate"
        ],
        "vaccines": ["Rabies Vaccine"],
        "travel_methods": ["Cabin travel (small breeds)", "Cargo transport"],
        "tips": [
            "Japan is a rabies-free country, which simplifies US import.",
            "Submit CDC form online to receive your import code by email."
        ]
    },
    {
        "from_country": "UK",
        "to_country": "USA",
        "pet_type": "cat",
        "slug": "uk-to-usa-cat",
        "title": "Bring a Cat from the UK to the USA (2026 Guide)",
        "summary": "Requirements for importing a cat from the United Kingdom to the United States.",
        "min_age": "No minimum for cats",
        "microchip": "ISO 11784/85 required",
        "rabies_vaccine": "Recommended",
        "quarantine": "No",
        "process_steps": [
            "Ensure microchip is ISO 11784/85 compliant",
            "Obtain rabies vaccination",
            "Get health certificate from UK-licensed vet",
            "Have certificate endorsed by APHA (UK authority)",
            "Travel with documents"
        ],
        "required_documents": [
            "APHA-endorsed Health Certificate",
            "Rabies Vaccination Certificate",
            "Microchip Record"
        ],
        "vaccines": ["Rabies Vaccine"],
        "travel_methods": ["Cabin travel", "Cargo transport", "Pet courier"],
        "tips": [
            "UK cats need an APHA-endorsed certificate; book vet appointment 10 days before travel.",
            "Non-EU format health certificates are required post-Brexit."
        ]
    },
    {
        "from_country": "UK",
        "to_country": "USA",
        "pet_type": "dog",
        "slug": "uk-to-usa-dog",
        "title": "Bring a Dog from the UK to the USA (2026 Guide)",
        "summary": "CDC and USDA requirements for importing a dog from the UK to the United States.",
        "min_age": "6 months",
        "microchip": "ISO 11784/85 required",
        "rabies_vaccine": "Required",
        "quarantine": "No (if vaccinated)",
        "process_steps": [
            "Microchip the dog",
            "Vaccinate against rabies",
            "Complete CDC Dog Import Form online",
            "Get health certificate from UK vet (APHA endorsed)",
            "Present CDC Import Code at US entry"
        ],
        "required_documents": [
            "CDC Dog Import Form",
            "APHA-endorsed Health Certificate",
            "Rabies Vaccination Certificate",
            "Microchip Documentation"
        ],
        "vaccines": ["Rabies Vaccine"],
        "travel_methods": ["Cargo transport", "Cabin travel (small breeds)"],
        "tips": [
            "The UK is considered low-risk for rabies; import process is streamlined.",
            "Ensure your health certificate is dated within 10 days of travel."
        ]
    },
    {
        "from_country": "Australia",
        "to_country": "USA",
        "pet_type": "cat",
        "slug": "australia-to-usa-cat",
        "title": "Bring a Cat from Australia to the USA (2026 Guide)",
        "summary": "Requirements for importing a cat from Australia to the United States.",
        "min_age": "No minimum for cats",
        "microchip": "ISO 11784/85 required",
        "rabies_vaccine": "Recommended",
        "quarantine": "No",
        "process_steps": [
            "Microchip the cat with ISO chip",
            "Obtain rabies vaccination",
            "Get health certificate from AQIS-accredited vet",
            "Book direct or connecting flight to USA",
            "Declare pet at US customs"
        ],
        "required_documents": [
            "Australian Government Health Certificate",
            "Rabies Vaccination Certificate",
            "Microchip Record"
        ],
        "vaccines": ["Rabies Vaccine"],
        "travel_methods": ["Cargo transport (long haul)", "Pet relocation service"],
        "tips": [
            "Australia is rabies-free; US entry is relatively smooth.",
            "Long flight times mean cargo is often more comfortable for cats."
        ]
    },
    {
        "from_country": "Australia",
        "to_country": "USA",
        "pet_type": "dog",
        "slug": "australia-to-usa-dog",
        "title": "Bring a Dog from Australia to the USA (2026 Guide)",
        "summary": "CDC and USDA requirements for importing a dog from Australia to the United States.",
        "min_age": "6 months",
        "microchip": "ISO 11784/85 required",
        "rabies_vaccine": "Required",
        "quarantine": "No (if vaccinated)",
        "process_steps": [
            "Microchip the dog",
            "Administer rabies vaccination",
            "Complete CDC Dog Import Form online",
            "Obtain AQIS-endorsed health certificate",
            "Present CDC Import Code at US entry"
        ],
        "required_documents": [
            "CDC Dog Import Form",
            "AQIS-endorsed Health Certificate",
            "Rabies Vaccination Certificate",
            "Microchip Documentation"
        ],
        "vaccines": ["Rabies Vaccine"],
        "travel_methods": ["Cargo transport", "Pet courier service"],
        "tips": [
            "Australia to USA is a long journey; ensure your dog is fit to fly.",
            "Use IATA-approved crates for cargo travel."
        ]
    },
    {
        "from_country": "Canada",
        "to_country": "USA",
        "pet_type": "cat",
        "slug": "canada-to-usa-cat",
        "title": "Bring a Cat from Canada to the USA (2026 Guide)",
        "summary": "Requirements for importing a cat from Canada to the United States.",
        "min_age": "No minimum for cats",
        "microchip": "Recommended",
        "rabies_vaccine": "Recommended",
        "quarantine": "No",
        "process_steps": [
            "Obtain health certificate from licensed Canadian vet",
            "Vaccinate against rabies (recommended)",
            "Cross the border with health certificate",
            "Declare pet at US customs"
        ],
        "required_documents": [
            "Veterinary Health Certificate",
            "Rabies Vaccination Certificate (recommended)"
        ],
        "vaccines": ["Rabies Vaccine (recommended)"],
        "travel_methods": ["Cabin travel", "Cargo transport", "Road travel across border"],
        "tips": [
            "Canada-to-USA cat import is one of the simplest internationally.",
            "Health certificate should be dated within 10 days of travel."
        ]
    },
    {
        "from_country": "Canada",
        "to_country": "USA",
        "pet_type": "dog",
        "slug": "canada-to-usa-dog",
        "title": "Bring a Dog from Canada to the USA (2026 Guide)",
        "summary": "CDC and USDA requirements for importing a dog from Canada to the United States.",
        "min_age": "6 months",
        "microchip": "Recommended",
        "rabies_vaccine": "Required",
        "quarantine": "No",
        "process_steps": [
            "Vaccinate dog against rabies in Canada",
            "Complete CDC Dog Import Form",
            "Obtain health certificate from Canadian vet",
            "Present CDC Import Code at US border crossing"
        ],
        "required_documents": [
            "CDC Dog Import Form",
            "Rabies Vaccination Certificate",
            "Veterinary Health Certificate"
        ],
        "vaccines": ["Rabies Vaccine"],
        "travel_methods": ["Road travel across border", "Cabin travel", "Cargo transport"],
        "tips": [
            "Canada is considered low-risk; the process is simpler than most countries.",
            "CDC form must be submitted before travel."
        ]
    },
    {
        "from_country": "Germany",
        "to_country": "USA",
        "pet_type": "cat",
        "slug": "germany-to-usa-cat",
        "title": "Bring a Cat from Germany to the USA (2026 Guide)",
        "summary": "Requirements for importing a cat from Germany to the United States.",
        "min_age": "No minimum for cats",
        "microchip": "ISO 11784/85 required",
        "rabies_vaccine": "Required",
        "quarantine": "No",
        "process_steps": [
            "Microchip the cat (EU standard, ISO compatible)",
            "Administer rabies vaccination",
            "Obtain EU-format health certificate",
            "Have certificate endorsed by German veterinary authority",
            "Travel with all documentation"
        ],
        "required_documents": [
            "EU Animal Health Certificate",
            "Rabies Vaccination Certificate",
            "Microchip Record"
        ],
        "vaccines": ["Rabies Vaccine"],
        "travel_methods": ["Cabin travel", "Cargo transport"],
        "tips": [
            "EU pet passports are not accepted in the USA; a separate health certificate is required.",
            "Book airport-to-airport pet transport through your airline."
        ]
    },
    {
        "from_country": "Germany",
        "to_country": "USA",
        "pet_type": "dog",
        "slug": "germany-to-usa-dog",
        "title": "Bring a Dog from Germany to the USA (2026 Guide)",
        "summary": "CDC and USDA requirements for importing a dog from Germany to the United States.",
        "min_age": "6 months",
        "microchip": "ISO 11784/85 required",
        "rabies_vaccine": "Required",
        "quarantine": "No (if vaccinated)",
        "process_steps": [
            "Microchip the dog",
            "Administer rabies vaccination",
            "Complete CDC Dog Import Form online",
            "Obtain German veterinary authority-endorsed health certificate",
            "Present all documents at US port of entry"
        ],
        "required_documents": [
            "CDC Dog Import Form",
            "German Authority-endorsed Health Certificate",
            "Rabies Vaccination Certificate",
            "Microchip Documentation"
        ],
        "vaccines": ["Rabies Vaccine"],
        "travel_methods": ["Cargo transport", "Cabin travel (small breeds)"],
        "tips": [
            "EU Pet Passports are NOT valid for US entry; you need a separate health certificate.",
            "Allow 4 weeks minimum for health certificate processing."
        ]
    },
    {
        "from_country": "France",
        "to_country": "USA",
        "pet_type": "cat",
        "slug": "france-to-usa-cat",
        "title": "Bring a Cat from France to the USA (2026 Guide)",
        "summary": "Requirements for importing a cat from France to the United States.",
        "min_age": "No minimum for cats",
        "microchip": "ISO 11784/85 required",
        "rabies_vaccine": "Required",
        "quarantine": "No",
        "process_steps": [
            "Ensure cat has ISO-compliant microchip",
            "Administer rabies vaccination",
            "Get health certificate from French vet",
            "Have certificate endorsed by DGAL (France)",
            "Travel with complete documentation"
        ],
        "required_documents": [
            "DGAL-endorsed Health Certificate",
            "Rabies Vaccination Certificate",
            "Microchip Record"
        ],
        "vaccines": ["Rabies Vaccine"],
        "travel_methods": ["Cabin travel", "Cargo transport"],
        "tips": [
            "France to USA is straightforward; ensure DGAL endorsement is recent.",
            "Some airlines do not allow pets in cabin on transatlantic flights."
        ]
    },
    {
        "from_country": "France",
        "to_country": "USA",
        "pet_type": "dog",
        "slug": "france-to-usa-dog",
        "title": "Bring a Dog from France to the USA (2026 Guide)",
        "summary": "CDC and USDA requirements for importing a dog from France to the United States.",
        "min_age": "6 months",
        "microchip": "ISO 11784/85 required",
        "rabies_vaccine": "Required",
        "quarantine": "No (if vaccinated)",
        "process_steps": [
            "Microchip the dog",
            "Vaccinate against rabies",
            "Complete CDC Dog Import Form online",
            "Get DGAL-endorsed health certificate",
            "Present CDC Import Code at entry"
        ],
        "required_documents": [
            "CDC Dog Import Form",
            "DGAL-endorsed Health Certificate",
            "Rabies Vaccination Certificate",
            "Microchip Documentation"
        ],
        "vaccines": ["Rabies Vaccine"],
        "travel_methods": ["Cargo transport", "Pet courier"],
        "tips": [
            "France is low-risk for rabies; process is similar to other EU countries.",
            "Cargo is the most common option for dogs on transatlantic flights."
        ]
    },
    {
        "from_country": "India",
        "to_country": "USA",
        "pet_type": "cat",
        "slug": "india-to-usa-cat",
        "title": "Bring a Cat from India to the USA (2026 Guide)",
        "summary": "Requirements for importing a cat from India to the United States.",
        "min_age": "No minimum for cats",
        "microchip": "ISO 11784/85 required",
        "rabies_vaccine": "Required",
        "quarantine": "No",
        "process_steps": [
            "Microchip the cat",
            "Administer rabies vaccination",
            "Obtain health certificate from Indian licensed vet",
            "Have certificate endorsed by DAHD (India)",
            "Export permit from DAHD",
            "Arrive at US port with all documents"
        ],
        "required_documents": [
            "DAHD-endorsed Health Certificate",
            "Export Permit (DAHD)",
            "Rabies Vaccination Certificate",
            "Microchip Record"
        ],
        "vaccines": ["Rabies Vaccine", "Feline Panleukopenia (recommended)"],
        "travel_methods": ["Cargo transport", "Pet courier service"],
        "tips": [
            "India has endemic rabies; ensure complete vaccination records are available.",
            "Allow extra time for DAHD endorsement (can take 1-2 weeks)."
        ]
    },
    {
        "from_country": "India",
        "to_country": "USA",
        "pet_type": "dog",
        "slug": "india-to-usa-dog",
        "title": "Bring a Dog from India to the USA (2026 Guide)",
        "summary": "CDC and USDA requirements for importing a dog from India to the United States.",
        "min_age": "6 months",
        "microchip": "ISO 11784/85 required",
        "rabies_vaccine": "Required (CDC-approved facility)",
        "quarantine": "Possible (if not from CDC-approved facility)",
        "process_steps": [
            "Microchip the dog",
            "Vaccinate at CDC-approved facility in India",
            "Complete CDC Dog Import Form online",
            "Obtain DAHD-endorsed health certificate",
            "Obtain export permit from DAHD",
            "Present all documents at US entry"
        ],
        "required_documents": [
            "CDC Dog Import Form",
            "DAHD-endorsed Health Certificate",
            "CDC-approved Rabies Vaccination Proof",
            "Export Permit (DAHD)",
            "Microchip Documentation"
        ],
        "vaccines": ["Rabies Vaccine (CDC-approved facility)", "DHPP recommended"],
        "travel_methods": ["Cargo transport", "Pet relocation service"],
        "tips": [
            "India requires CDC-approved facility vaccination; verify current approved list.",
            "Plan at least 6 months ahead for the complete process."
        ]
    },
    {
        "from_country": "South Korea",
        "to_country": "USA",
        "pet_type": "cat",
        "slug": "south-korea-to-usa-cat",
        "title": "Bring a Cat from South Korea to the USA (2026 Guide)",
        "summary": "Requirements for importing a cat from South Korea to the United States.",
        "min_age": "No minimum for cats",
        "microchip": "ISO 11784/85 required",
        "rabies_vaccine": "Required",
        "quarantine": "No",
        "process_steps": [
            "Microchip the cat",
            "Administer rabies vaccination",
            "Obtain health certificate from Korean vet",
            "Get MAFRA endorsement on health certificate",
            "Travel with complete documents"
        ],
        "required_documents": [
            "MAFRA-endorsed Health Certificate",
            "Rabies Vaccination Certificate",
            "Microchip Record"
        ],
        "vaccines": ["Rabies Vaccine"],
        "travel_methods": ["Cabin travel", "Cargo transport"],
        "tips": [
            "South Korea has controlled rabies status; process is relatively smooth.",
            "MAFRA endorsement typically takes 3-5 business days."
        ]
    },
    {
        "from_country": "South Korea",
        "to_country": "USA",
        "pet_type": "dog",
        "slug": "south-korea-to-usa-dog",
        "title": "Bring a Dog from South Korea to the USA (2026 Guide)",
        "summary": "CDC requirements for importing a dog from South Korea to the United States.",
        "min_age": "6 months",
        "microchip": "ISO 11784/85 required",
        "rabies_vaccine": "Required",
        "quarantine": "No (if vaccinated)",
        "process_steps": [
            "Microchip the dog",
            "Vaccinate against rabies",
            "Complete CDC Dog Import Form online",
            "Obtain MAFRA-endorsed health certificate",
            "Present CDC Import Code at US entry"
        ],
        "required_documents": [
            "CDC Dog Import Form",
            "MAFRA-endorsed Health Certificate",
            "Rabies Vaccination Certificate",
            "Microchip Documentation"
        ],
        "vaccines": ["Rabies Vaccine"],
        "travel_methods": ["Cargo transport", "Cabin travel (small breeds)"],
        "tips": [
            "CDC form must be completed before departure.",
            "Many Korean airlines have direct routes to major US cities."
        ]
    },
    {
        "from_country": "Mexico",
        "to_country": "USA",
        "pet_type": "cat",
        "slug": "mexico-to-usa-cat",
        "title": "Bring a Cat from Mexico to the USA (2026 Guide)",
        "summary": "Requirements for importing a cat from Mexico to the United States.",
        "min_age": "No minimum for cats",
        "microchip": "Recommended",
        "rabies_vaccine": "Recommended",
        "quarantine": "No",
        "process_steps": [
            "Obtain health certificate from Mexican licensed vet",
            "Vaccinate against rabies (recommended)",
            "Cross US border with health certificate",
            "Declare pet at US customs"
        ],
        "required_documents": [
            "Veterinary Health Certificate",
            "Rabies Vaccination Certificate (recommended)"
        ],
        "vaccines": ["Rabies Vaccine (recommended)"],
        "travel_methods": ["Road travel across border", "Cabin travel", "Cargo"],
        "tips": [
            "Cat import from Mexico is relatively simple.",
            "Ensure the health certificate is in English or with translation."
        ]
    },
    {
        "from_country": "Mexico",
        "to_country": "USA",
        "pet_type": "dog",
        "slug": "mexico-to-usa-dog",
        "title": "Bring a Dog from Mexico to the USA (2026 Guide)",
        "summary": "CDC requirements for importing a dog from Mexico to the United States.",
        "min_age": "6 months",
        "microchip": "Required",
        "rabies_vaccine": "Required",
        "quarantine": "Possible",
        "process_steps": [
            "Microchip the dog",
            "Vaccinate against rabies",
            "Complete CDC Dog Import Form online",
            "Obtain health certificate from Mexican vet",
            "Present CDC Import Code at US border"
        ],
        "required_documents": [
            "CDC Dog Import Form",
            "Rabies Vaccination Certificate",
            "Veterinary Health Certificate",
            "Microchip Documentation"
        ],
        "vaccines": ["Rabies Vaccine"],
        "travel_methods": ["Road travel across border", "Cargo transport"],
        "tips": [
            "Mexico is considered high-risk for dog rabies; ensure CDC form is completed.",
            "Dogs vaccinated in Mexico need additional documentation for CDC compliance."
        ]
    },
    {
        "from_country": "Brazil",
        "to_country": "USA",
        "pet_type": "dog",
        "slug": "brazil-to-usa-dog",
        "title": "Bring a Dog from Brazil to the USA (2026 Guide)",
        "summary": "CDC and USDA requirements for importing a dog from Brazil to the United States.",
        "min_age": "6 months",
        "microchip": "ISO 11784/85 required",
        "rabies_vaccine": "Required",
        "quarantine": "No (if vaccinated)",
        "process_steps": [
            "Microchip the dog",
            "Administer rabies vaccination",
            "Complete CDC Dog Import Form online",
            "Get MAPA-endorsed health certificate",
            "Present all documents at US entry"
        ],
        "required_documents": [
            "CDC Dog Import Form",
            "MAPA-endorsed Health Certificate",
            "Rabies Vaccination Certificate",
            "Microchip Documentation"
        ],
        "vaccines": ["Rabies Vaccine"],
        "travel_methods": ["Cargo transport", "Pet relocation service"],
        "tips": [
            "Brazil has controlled rabies; standard CDC process applies.",
            "MAPA endorsement can take up to 2 weeks during busy periods."
        ]
    },
    {
        "from_country": "New Zealand",
        "to_country": "USA",
        "pet_type": "cat",
        "slug": "new-zealand-to-usa-cat",
        "title": "Bring a Cat from New Zealand to the USA (2026 Guide)",
        "summary": "Requirements for importing a cat from New Zealand to the United States.",
        "min_age": "No minimum for cats",
        "microchip": "ISO 11784/85 required",
        "rabies_vaccine": "Recommended",
        "quarantine": "No",
        "process_steps": [
            "Microchip the cat",
            "Obtain rabies vaccination",
            "Get health certificate from NZ licensed vet",
            "Have certificate endorsed by MPI (NZ)",
            "Arrange cargo or cabin travel"
        ],
        "required_documents": [
            "MPI-endorsed Health Certificate",
            "Rabies Vaccination Certificate",
            "Microchip Record"
        ],
        "vaccines": ["Rabies Vaccine (recommended)"],
        "travel_methods": ["Cargo transport (long haul)", "Pet courier"],
        "tips": [
            "New Zealand is rabies-free; import to USA is simpler than most countries.",
            "Long flight times mean planning for pet comfort is essential."
        ]
    },
    {
        "from_country": "Singapore",
        "to_country": "USA",
        "pet_type": "dog",
        "slug": "singapore-to-usa-dog",
        "title": "Bring a Dog from Singapore to the USA (2026 Guide)",
        "summary": "CDC requirements for importing a dog from Singapore to the United States.",
        "min_age": "6 months",
        "microchip": "ISO 11784/85 required",
        "rabies_vaccine": "Required",
        "quarantine": "No (if vaccinated)",
        "process_steps": [
            "Microchip the dog",
            "Vaccinate against rabies",
            "Complete CDC Dog Import Form online",
            "Get AVS-endorsed health certificate",
            "Present CDC Import Code at US entry"
        ],
        "required_documents": [
            "CDC Dog Import Form",
            "AVS-endorsed Health Certificate",
            "Rabies Vaccination Certificate",
            "Microchip Documentation"
        ],
        "vaccines": ["Rabies Vaccine"],
        "travel_methods": ["Cargo transport", "Cabin travel (small breeds)"],
        "tips": [
            "Singapore is considered low rabies risk; standard process applies.",
            "Singapore Airlines has good pet transport services."
        ]
    }
]

# ─────────────────────────────────────────────
# HELPER
# ─────────────────────────────────────────────

def write(path: str, content: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ {path}")


def p(*parts):
    return os.path.join(BASE_DIR, *parts)


# ─────────────────────────────────────────────
# DATA FILES
# ─────────────────────────────────────────────

def gen_data():
    print("\n[1/9] Writing route JSON data...")
    for route in ROUTES:
        write(p("data", "routes", f"{route['slug']}.json"), json.dumps(route, indent=2))


# ─────────────────────────────────────────────
# PACKAGE.JSON & CONFIG
# ─────────────────────────────────────────────

def gen_package_json():
    print("\n[2/9] Writing package.json and config files...")
    write(p("package.json"), json.dumps({
        "name": "petentryguide",
        "version": "0.1.0",
        "private": True,
        "scripts": {
            "dev": "next dev",
            "build": "next build",
            "start": "next start",
            "lint": "next lint"
        },
        "dependencies": {
            "next": "14.2.5",
            "react": "^18",
            "react-dom": "^18"
        },
        "devDependencies": {
            "@types/node": "^20",
            "@types/react": "^18",
            "@types/react-dom": "^18",
            "autoprefixer": "^10.0.1",
            "postcss": "^8",
            "tailwindcss": "^3.4.1",
            "typescript": "^5"
        }
    }, indent=2))

    write(p("next.config.mjs"), """\
/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
};

export default nextConfig;
""")

    write(p("tsconfig.json"), json.dumps({
        "compilerOptions": {
            "lib": ["dom", "dom.iterable", "esnext"],
            "allowJs": True,
            "skipLibCheck": True,
            "strict": True,
            "noEmit": True,
            "esModuleInterop": True,
            "module": "esnext",
            "moduleResolution": "bundler",
            "resolveJsonModule": True,
            "isolatedModules": True,
            "jsx": "preserve",
            "incremental": True,
            "plugins": [{"name": "next"}],
            "paths": {"@/*": ["./*"]}
        },
        "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
        "exclude": ["node_modules"]
    }, indent=2))

    write(p("tailwind.config.ts"), """\
import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['var(--font-inter)', 'system-ui', 'sans-serif'],
        mono: ['var(--font-mono)', 'monospace'],
      },
      colors: {
        brand: {
          50:  '#f0f9ff',
          100: '#e0f2fe',
          200: '#bae6fd',
          300: '#7dd3fc',
          400: '#38bdf8',
          500: '#0ea5e9',
          600: '#0284c7',
          700: '#0369a1',
          800: '#075985',
          900: '#0c4a6e',
        }
      }
    },
  },
  plugins: [],
}
export default config
""")

    write(p("postcss.config.mjs"), """\
/** @type {import('postcss').Config} */
const config = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};

export default config;
""")


# ─────────────────────────────────────────────
# LIB
# ─────────────────────────────────────────────

def gen_lib():
    print("\n[3/9] Writing lib/getRoutes.ts...")
    write(p("lib", "getRoutes.ts"), """\
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
""")


# ─────────────────────────────────────────────
# COMPONENTS
# ─────────────────────────────────────────────

def gen_components():
    print("\n[4/9] Writing components...")

    # HeroSearch
    write(p("components", "HeroSearch.tsx"), """\
'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';

const FROM_COUNTRIES = [
  'Australia','Brazil','Canada','China','France','Germany',
  'India','Japan','Mexico','New Zealand','Singapore','South Korea','UK'
];
const TO_COUNTRIES = ['USA'];
const PET_TYPES    = ['cat','dog'];

export default function HeroSearch() {
  const router = useRouter();
  const [from, setFrom] = useState('');
  const [to, setTo]     = useState('USA');
  const [pet, setPet]   = useState('');
  const [error, setError] = useState('');

  const handleSearch = () => {
    if (!from || !to || !pet) {
      setError('Please select all three options.');
      return;
    }
    setError('');
    const slug = `${from.toLowerCase().replace(/\\s+/g,'-')}-to-${to.toLowerCase()}-${pet}`;
    router.push(`/${slug}`);
  };

  return (
    <div className="bg-white rounded-2xl shadow-lg border border-slate-200 p-8 max-w-2xl mx-auto">
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-4">
        <div>
          <label className="block text-xs font-semibold text-slate-500 mb-1 uppercase tracking-wide">From Country</label>
          <select
            value={from}
            onChange={e => setFrom(e.target.value)}
            className="w-full border border-slate-200 rounded-lg px-3 py-2.5 text-slate-800 bg-slate-50 focus:outline-none focus:ring-2 focus:ring-brand-500 text-sm"
          >
            <option value="">Select country</option>
            {FROM_COUNTRIES.map(c => <option key={c} value={c}>{c}</option>)}
          </select>
        </div>
        <div>
          <label className="block text-xs font-semibold text-slate-500 mb-1 uppercase tracking-wide">To Country</label>
          <select
            value={to}
            onChange={e => setTo(e.target.value)}
            className="w-full border border-slate-200 rounded-lg px-3 py-2.5 text-slate-800 bg-slate-50 focus:outline-none focus:ring-2 focus:ring-brand-500 text-sm"
          >
            {TO_COUNTRIES.map(c => <option key={c} value={c}>{c}</option>)}
          </select>
        </div>
        <div>
          <label className="block text-xs font-semibold text-slate-500 mb-1 uppercase tracking-wide">Pet Type</label>
          <select
            value={pet}
            onChange={e => setPet(e.target.value)}
            className="w-full border border-slate-200 rounded-lg px-3 py-2.5 text-slate-800 bg-slate-50 focus:outline-none focus:ring-2 focus:ring-brand-500 text-sm capitalize"
          >
            <option value="">Select pet</option>
            {PET_TYPES.map(p => <option key={p} value={p} className="capitalize">{p.charAt(0).toUpperCase()+p.slice(1)}</option>)}
          </select>
        </div>
      </div>
      {error && <p className="text-red-500 text-sm mb-3">{error}</p>}
      <button
        onClick={handleSearch}
        className="w-full bg-brand-600 hover:bg-brand-700 text-white font-semibold py-3 px-6 rounded-xl transition-colors duration-150 text-sm"
      >
        Search Requirements →
      </button>
    </div>
  );
}
""")

    # RouteCard
    write(p("components", "RouteCard.tsx"), """\
import Link from 'next/link';

interface RouteCardProps {
  from: string;
  to: string;
  petType: string;
  slug: string;
}

export default function RouteCard({ from, to, petType, slug }: RouteCardProps) {
  const emoji = petType === 'cat' ? '🐱' : '🐶';
  return (
    <Link href={`/${slug}`}
      className="block bg-white border border-slate-200 rounded-xl p-5 hover:border-brand-400 hover:shadow-md transition-all duration-150 group"
    >
      <div className="flex items-center gap-3 mb-2">
        <span className="text-2xl">{emoji}</span>
        <span className="font-semibold text-slate-800 capitalize">{petType}</span>
      </div>
      <div className="text-sm text-slate-500">
        <span className="font-medium text-slate-700">{from}</span>
        <span className="mx-2 text-slate-400">→</span>
        <span className="font-medium text-slate-700">{to}</span>
      </div>
      <div className="mt-3 text-xs text-brand-600 font-medium group-hover:underline">View requirements →</div>
    </Link>
  );
}
""")

    # SummaryGrid
    write(p("components", "SummaryGrid.tsx"), """\
interface Item {
  label: string;
  value: string;
  status?: 'ok' | 'warn' | 'neutral';
}

export default function SummaryGrid({ items }: { items: Item[] }) {
  const color = (s?: string) => {
    if (s === 'ok')   return 'text-emerald-700 bg-emerald-50 border-emerald-200';
    if (s === 'warn') return 'text-amber-700 bg-amber-50 border-amber-200';
    return 'text-slate-700 bg-slate-50 border-slate-200';
  };
  return (
    <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
      {items.map(item => (
        <div key={item.label} className={`rounded-xl border p-4 ${color(item.status)}`}>
          <div className="text-xs font-semibold uppercase tracking-wide opacity-70 mb-1">{item.label}</div>
          <div className="text-sm font-bold">{item.value}</div>
        </div>
      ))}
    </div>
  );
}
""")

    # ProcessSteps
    write(p("components", "ProcessSteps.tsx"), """\
export default function ProcessSteps({ steps }: { steps: string[] }) {
  return (
    <ol className="space-y-3">
      {steps.map((step, i) => (
        <li key={i} className="flex gap-4 items-start">
          <span className="flex-shrink-0 w-7 h-7 rounded-full bg-brand-600 text-white text-xs font-bold flex items-center justify-center mt-0.5">
            {i + 1}
          </span>
          <span className="text-slate-700 text-sm leading-relaxed pt-1">{step}</span>
        </li>
      ))}
    </ol>
  );
}
""")

    # DocumentList
    write(p("components", "DocumentList.tsx"), """\
export default function DocumentList({ documents }: { documents: string[] }) {
  return (
    <ul className="space-y-2">
      {documents.map((doc, i) => (
        <li key={i} className="flex items-start gap-3 text-sm text-slate-700">
          <span className="text-brand-500 mt-0.5">📄</span>
          <span>{doc}</span>
        </li>
      ))}
    </ul>
  );
}
""")

    # Breadcrumb
    write(p("components", "Breadcrumb.tsx"), """\
import Link from 'next/link';

interface Crumb {
  label: string;
  href?: string;
}

export default function Breadcrumb({ crumbs }: { crumbs: Crumb[] }) {
  return (
    <nav className="text-sm text-slate-500 mb-6 flex flex-wrap gap-1 items-center">
      {crumbs.map((crumb, i) => (
        <span key={i} className="flex items-center gap-1">
          {i > 0 && <span className="text-slate-300">›</span>}
          {crumb.href
            ? <Link href={crumb.href} className="hover:text-brand-600 transition-colors">{crumb.label}</Link>
            : <span className="text-slate-800 font-medium">{crumb.label}</span>
          }
        </span>
      ))}
    </nav>
  );
}
""")

    # Navbar
    write(p("components", "Navbar.tsx"), """\
import Link from 'next/link';

export default function Navbar() {
  return (
    <header className="border-b border-slate-200 bg-white sticky top-0 z-50">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 h-14 flex items-center justify-between">
        <Link href="/" className="flex items-center gap-2 font-bold text-slate-900 text-lg">
          <span className="text-2xl">🐾</span>
          <span>PetEntryGuide</span>
        </Link>
        <nav className="flex items-center gap-6 text-sm text-slate-600">
          <Link href="/pet-travel-checklist" className="hover:text-brand-600 transition-colors">Checklist</Link>
          <Link href="/pet-cargo-travel-guide" className="hover:text-brand-600 transition-colors">Cargo Guide</Link>
          <Link href="/rabies-vaccine-requirements" className="hover:text-brand-600 transition-colors">Rabies Rules</Link>
        </nav>
      </div>
    </header>
  );
}
""")

    # Footer
    write(p("components", "Footer.tsx"), """\
import Link from 'next/link';

export default function Footer() {
  return (
    <footer className="border-t border-slate-200 bg-slate-50 mt-16">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 py-10">
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-8 text-sm">
          <div>
            <div className="font-bold text-slate-900 mb-3 flex items-center gap-2">
              <span className="text-xl">🐾</span> PetEntryGuide
            </div>
            <p className="text-slate-500 leading-relaxed">
              Structured import rules and travel requirements for pets worldwide.
            </p>
          </div>
          <div>
            <div className="font-semibold text-slate-700 mb-3">Guides</div>
            <ul className="space-y-2 text-slate-500">
              <li><Link href="/pet-travel-checklist" className="hover:text-brand-600">Pet Travel Checklist</Link></li>
              <li><Link href="/cost-to-bring-cat-to-usa" className="hover:text-brand-600">Cost to Bring Cat to USA</Link></li>
              <li><Link href="/pet-cargo-travel-guide" className="hover:text-brand-600">Pet Cargo Travel Guide</Link></li>
            </ul>
          </div>
          <div>
            <div className="font-semibold text-slate-700 mb-3">Rules</div>
            <ul className="space-y-2 text-slate-500">
              <li><Link href="/rabies-vaccine-requirements" className="hover:text-brand-600">Rabies Vaccine Requirements</Link></li>
              <li><Link href="/cdc-dog-import-rule" className="hover:text-brand-600">CDC Dog Import Rule</Link></li>
              <li><Link href="/usda-accredited-vet" className="hover:text-brand-600">USDA Accredited Vet</Link></li>
            </ul>
          </div>
        </div>
        <div className="border-t border-slate-200 mt-8 pt-6 text-xs text-slate-400">
          © 2026 PetEntryGuide.com — For informational purposes only. Always verify with official government sources.
        </div>
      </div>
    </footer>
  );
}
""")


# ─────────────────────────────────────────────
# APP: LAYOUT + GLOBAL CSS
# ─────────────────────────────────────────────

def gen_app_shell():
    print("\n[5/9] Writing app shell (layout, globals)...")
    write(p("app", "globals.css"), """\
@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --font-inter: 'Inter', system-ui, sans-serif;
}

body {
  @apply bg-slate-50 text-slate-900 antialiased;
}
""")

    write(p("app", "layout.tsx"), """\
import type { Metadata } from 'next';
import './globals.css';
import Navbar from '@/components/Navbar';
import Footer from '@/components/Footer';

export const metadata: Metadata = {
  title: {
    default: 'PetEntryGuide – International Pet Import Requirements',
    template: '%s | PetEntryGuide',
  },
  description: 'Find official import requirements for traveling internationally with pets. Step-by-step guides for every route.',
  metadataBase: new URL('https://petentryguide.com'),
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
      </head>
      <body>
        <Navbar />
        <main>{children}</main>
        <Footer />
      </body>
    </html>
  );
}
""")


# ─────────────────────────────────────────────
# APP: HOME PAGE
# ─────────────────────────────────────────────

POPULAR_ROUTES = [
    {"from": "China",   "to": "USA", "cat_slug": "china-to-usa-cat",     "dog_slug": "china-to-usa-dog"},
    {"from": "Japan",   "to": "USA", "cat_slug": "japan-to-usa-cat",     "dog_slug": "japan-to-usa-dog"},
    {"from": "UK",      "to": "USA", "cat_slug": "uk-to-usa-cat",        "dog_slug": "uk-to-usa-dog"},
    {"from": "Canada",  "to": "USA", "cat_slug": "canada-to-usa-cat",    "dog_slug": "canada-to-usa-dog"},
    {"from": "Germany", "to": "USA", "cat_slug": "germany-to-usa-cat",   "dog_slug": "germany-to-usa-dog"},
    {"from": "India",   "to": "USA", "cat_slug": "india-to-usa-cat",     "dog_slug": "india-to-usa-dog"},
]


def gen_home():
    print("\n[6/9] Writing home page...")

    popular_cards = "\n".join([
        f"""        <div key="{r['from']}" className="bg-white border border-slate-200 rounded-xl p-5">
          <div className="font-semibold text-slate-800 mb-1">{r['from']} <span className="text-slate-400">→</span> {r['to']}</div>
          <div className="flex gap-3 mt-3">
            <Link href="/{r['cat_slug']}" className="flex-1 text-center text-xs font-medium bg-slate-50 hover:bg-brand-50 border border-slate-200 hover:border-brand-300 text-slate-700 hover:text-brand-700 py-1.5 rounded-lg transition-all">🐱 Cat</Link>
            <Link href="/{r['dog_slug']}" className="flex-1 text-center text-xs font-medium bg-slate-50 hover:bg-brand-50 border border-slate-200 hover:border-brand-300 text-slate-700 hover:text-brand-700 py-1.5 rounded-lg transition-all">🐶 Dog</Link>
          </div>
        </div>"""
        for r in POPULAR_ROUTES
    ])

    write(p("app", "page.tsx"), f"""\
import type {{ Metadata }} from 'next';
import Link from 'next/link';
import HeroSearch from '@/components/HeroSearch';

export const metadata: Metadata = {{
  title: 'Find Pet Import Requirements Worldwide | PetEntryGuide',
  description: 'Search official import rules for traveling internationally with pets. Step-by-step guides for dogs and cats from any country.',
  alternates: {{ canonical: 'https://petentryguide.com' }},
}};

export default function HomePage() {{
  return (
    <div>
      {{/* Hero */}}
      <section className="bg-gradient-to-b from-brand-900 to-brand-800 text-white py-20 px-4">
        <div className="max-w-3xl mx-auto text-center">
          <div className="inline-flex items-center gap-2 bg-brand-700/50 border border-brand-600 rounded-full px-4 py-1.5 text-xs font-medium mb-6 text-brand-200">
            🌍 2026 Updated Requirements
          </div>
          <h1 className="text-4xl sm:text-5xl font-bold mb-4 leading-tight">
            Find Pet Import Requirements<br />
            <span className="text-brand-300">Worldwide</span>
          </h1>
          <p className="text-brand-200 text-lg mb-10 max-w-xl mx-auto leading-relaxed">
            Search official import rules for traveling internationally with pets.
          </p>
          <HeroSearch />
        </div>
      </section>

      {{/* Popular Routes */}}
      <section className="max-w-5xl mx-auto px-4 sm:px-6 py-16">
        <h2 className="text-xl font-bold text-slate-900 mb-2">Popular Routes to the USA</h2>
        <p className="text-slate-500 text-sm mb-8">Click a route to view full import requirements for cats or dogs.</p>
        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-3 gap-4">
{popular_cards}
        </div>
      </section>

      {{/* Info Strip */}}
      <section className="bg-brand-50 border-y border-brand-100 py-12 px-4">
        <div className="max-w-5xl mx-auto grid grid-cols-1 sm:grid-cols-3 gap-8 text-center">
          <div>
            <div className="text-3xl mb-2">📋</div>
            <div className="font-semibold text-slate-800 mb-1">Step-by-Step Process</div>
            <p className="text-slate-500 text-sm">Every guide includes an ordered checklist of required steps.</p>
          </div>
          <div>
            <div className="text-3xl mb-2">📄</div>
            <div className="font-semibold text-slate-800 mb-1">Required Documents</div>
            <p className="text-slate-500 text-sm">Know exactly which documents to prepare before you travel.</p>
          </div>
          <div>
            <div className="text-3xl mb-2">💡</div>
            <div className="font-semibold text-slate-800 mb-1">Expert Tips</div>
            <p className="text-slate-500 text-sm">Practical advice from experienced pet travel professionals.</p>
          </div>
        </div>
      </section>

      {{/* Rule Pages */}}
      <section className="max-w-5xl mx-auto px-4 sm:px-6 py-16">
        <h2 className="text-xl font-bold text-slate-900 mb-6">Important Rules & Regulations</h2>
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
          <Link href="/rabies-vaccine-requirements" className="block bg-white border border-slate-200 rounded-xl p-5 hover:border-brand-300 hover:shadow-sm transition-all">
            <div className="text-2xl mb-2">💉</div>
            <div className="font-semibold text-slate-800 mb-1">Rabies Vaccine Requirements</div>
            <p className="text-slate-500 text-xs">Global vaccination rules for international pet travel.</p>
          </Link>
          <Link href="/cdc-dog-import-rule" className="block bg-white border border-slate-200 rounded-xl p-5 hover:border-brand-300 hover:shadow-sm transition-all">
            <div className="text-2xl mb-2">🏛️</div>
            <div className="font-semibold text-slate-800 mb-1">CDC Dog Import Rule</div>
            <p className="text-slate-500 text-xs">USA CDC requirements for importing dogs from abroad.</p>
          </Link>
          <Link href="/usda-accredited-vet" className="block bg-white border border-slate-200 rounded-xl p-5 hover:border-brand-300 hover:shadow-sm transition-all">
            <div className="text-2xl mb-2">🩺</div>
            <div className="font-semibold text-slate-800 mb-1">USDA Accredited Vet</div>
            <p className="text-slate-500 text-xs">Why you need a USDA-accredited vet for export health certificates.</p>
          </Link>
        </div>
      </section>
    </div>
  );
}}
""")


# ─────────────────────────────────────────────
# APP: DYNAMIC ROUTE PAGE [slug]
# ─────────────────────────────────────────────

def gen_slug_page():
    print("\n[7/9] Writing [slug] route page...")
    write(p("app", "[slug]", "page.tsx"), """\
import { notFound } from 'next/navigation';
import type { Metadata } from 'next';
import { getAllSlugs, getRouteBySlug } from '@/lib/getRoutes';
import SummaryGrid from '@/components/SummaryGrid';
import ProcessSteps from '@/components/ProcessSteps';
import DocumentList from '@/components/DocumentList';
import Breadcrumb from '@/components/Breadcrumb';

export async function generateStaticParams() {
  const slugs = getAllSlugs();
  return slugs.map(slug => ({ slug }));
}

export async function generateMetadata({ params }: { params: { slug: string } }): Promise<Metadata> {
  const route = getRouteBySlug(params.slug);
  if (!route) return { title: 'Not Found' };
  return {
    title: `${route.title} | PetEntryGuide`,
    description: route.summary,
    alternates: { canonical: `https://petentryguide.com/${route.slug}` },
    openGraph: {
      title: route.title,
      description: route.summary,
      url: `https://petentryguide.com/${route.slug}`,
      type: 'article',
    },
  };
}

export default function RouteGuidePage({ params }: { params: { slug: string } }) {
  const route = getRouteBySlug(params.slug);
  if (!route) notFound();

  const summaryItems = [
    {
      label: 'Minimum Age',
      value: route.min_age,
      status: 'neutral' as const,
    },
    {
      label: 'Microchip',
      value: route.microchip.includes('required') || route.microchip.includes('Required')
        ? 'Required' : route.microchip,
      status: (route.microchip.toLowerCase().includes('required') ? 'warn' : 'neutral') as const,
    },
    {
      label: 'Rabies Vaccine',
      value: route.rabies_vaccine,
      status: (route.rabies_vaccine.toLowerCase().includes('required') ? 'warn' : 'ok') as const,
    },
    {
      label: 'Quarantine',
      value: route.quarantine,
      status: (route.quarantine.toLowerCase() === 'no' ? 'ok' : 'warn') as const,
    },
  ];

  const petEmoji = route.pet_type === 'cat' ? '🐱' : '🐶';

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 py-10">
      <Breadcrumb crumbs={[
        { label: 'Home', href: '/' },
        { label: route.from_country },
        { label: route.to_country },
        { label: route.pet_type.charAt(0).toUpperCase() + route.pet_type.slice(1) },
      ]} />

      {/* Header */}
      <div className="mb-8">
        <div className="inline-flex items-center gap-2 text-xs font-semibold text-brand-600 bg-brand-50 border border-brand-200 rounded-full px-3 py-1 mb-4">
          {petEmoji} {route.from_country} → {route.to_country}
        </div>
        <h1 className="text-3xl sm:text-4xl font-bold text-slate-900 mb-3 leading-tight">
          {route.title}
        </h1>
        <p className="text-slate-500 text-base leading-relaxed max-w-2xl">{route.summary}</p>
      </div>

      {/* Quick Summary */}
      <section className="mb-10">
        <h2 className="text-lg font-bold text-slate-900 mb-4">Quick Requirements Summary</h2>
        <SummaryGrid items={summaryItems} />
      </section>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Main Content */}
        <div className="lg:col-span-2 space-y-10">

          {/* Process */}
          <section>
            <h2 className="text-lg font-bold text-slate-900 mb-4">Step-by-Step Process</h2>
            <div className="bg-white border border-slate-200 rounded-xl p-6">
              <ProcessSteps steps={route.process_steps} />
            </div>
          </section>

          {/* Documents */}
          <section>
            <h2 className="text-lg font-bold text-slate-900 mb-4">Required Documents</h2>
            <div className="bg-white border border-slate-200 rounded-xl p-6">
              <DocumentList documents={route.required_documents} />
            </div>
          </section>

          {/* Tips */}
          {route.tips.length > 0 && (
            <section>
              <h2 className="text-lg font-bold text-slate-900 mb-4">Expert Tips</h2>
              <div className="bg-amber-50 border border-amber-200 rounded-xl p-6 space-y-3">
                {route.tips.map((tip, i) => (
                  <div key={i} className="flex gap-3 text-sm text-amber-900">
                    <span className="text-amber-500 flex-shrink-0 mt-0.5">💡</span>
                    <span>{tip}</span>
                  </div>
                ))}
              </div>
            </section>
          )}
        </div>

        {/* Sidebar */}
        <div className="space-y-6">

          {/* Vaccines */}
          <div className="bg-white border border-slate-200 rounded-xl p-5">
            <h3 className="font-bold text-slate-800 mb-3 text-sm">💉 Vaccination Requirements</h3>
            <ul className="space-y-2">
              {route.vaccines.map((v, i) => (
                <li key={i} className="text-sm text-slate-700 flex items-start gap-2">
                  <span className="text-emerald-500 mt-0.5">✓</span> {v}
                </li>
              ))}
            </ul>
          </div>

          {/* Travel Methods */}
          <div className="bg-white border border-slate-200 rounded-xl p-5">
            <h3 className="font-bold text-slate-800 mb-3 text-sm">✈️ Travel Methods</h3>
            <ul className="space-y-2">
              {route.travel_methods.map((m, i) => (
                <li key={i} className="text-sm text-slate-700 flex items-start gap-2">
                  <span className="text-brand-400 mt-0.5">→</span> {m}
                </li>
              ))}
            </ul>
          </div>

          {/* Disclaimer */}
          <div className="bg-slate-50 border border-slate-200 rounded-xl p-5 text-xs text-slate-500 leading-relaxed">
            ⚠️ Requirements change frequently. Always verify with official government sources before travel.
          </div>
        </div>
      </div>
    </div>
  );
}
""")


# ─────────────────────────────────────────────
# STATIC PAGES (Rule + Practical)
# ─────────────────────────────────────────────

def gen_static_pages():
    print("\n[8/9] Writing static rule and practical pages...")

    # ── Rabies Vaccine Requirements
    write(p("app", "rabies-vaccine-requirements", "page.tsx"), """\
import type { Metadata } from 'next';
import Link from 'next/link';

export const metadata: Metadata = {
  title: 'Rabies Vaccine Requirements for International Pet Travel',
  description: 'Learn when and why a rabies vaccine is required to travel internationally with your pet, common mistakes, and which countries require it.',
  alternates: { canonical: 'https://petentryguide.com/rabies-vaccine-requirements' },
};

export default function RabiesPage() {
  return (
    <div className="max-w-3xl mx-auto px-4 sm:px-6 py-12">
      <div className="mb-8">
        <div className="inline-flex items-center gap-2 text-xs font-semibold text-brand-600 bg-brand-50 border border-brand-200 rounded-full px-3 py-1 mb-4">💉 Rule</div>
        <h1 className="text-3xl font-bold text-slate-900 mb-3">Rabies Vaccine Requirements</h1>
        <p className="text-slate-500 leading-relaxed">A rabies vaccination is one of the most universally required documents when importing pets internationally. This guide explains when it is mandatory, what proof is needed, and common mistakes to avoid.</p>
      </div>

      <div className="prose-sm max-w-none space-y-8">
        <section className="bg-white border border-slate-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-slate-900 mb-3">When is Rabies Vaccination Required?</h2>
          <p className="text-slate-600 leading-relaxed mb-3">The United States requires all imported dogs to have a valid rabies vaccination. For cats, it is strongly recommended and required by many airlines. Any country classified as high-risk for dog rabies by the CDC requires vaccination at a <strong>CDC-approved facility</strong>.</p>
          <ul className="space-y-2 text-slate-600 text-sm">
            <li className="flex gap-2"><span className="text-emerald-500">✓</span> Always required for dogs entering the USA</li>
            <li className="flex gap-2"><span className="text-emerald-500">✓</span> Required before microchipping is complete (chip must come first)</li>
            <li className="flex gap-2"><span className="text-emerald-500">✓</span> Booster shots must be within validity period</li>
          </ul>
        </section>

        <section className="bg-white border border-slate-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-slate-900 mb-3">What Proof is Needed?</h2>
          <p className="text-slate-600 leading-relaxed mb-3">You must carry an official rabies vaccination certificate issued by a licensed veterinarian. It should include:</p>
          <ul className="space-y-1 text-slate-600 text-sm list-disc list-inside">
            <li>Pet name, species, breed, and microchip number</li>
            <li>Vaccine brand, serial number, and expiry date</li>
            <li>Veterinarian's license number and signature</li>
            <li>Date of vaccination</li>
          </ul>
        </section>

        <section className="bg-amber-50 border border-amber-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-amber-900 mb-3">⚠️ Common Mistakes</h2>
          <ul className="space-y-2 text-amber-800 text-sm">
            <li className="flex gap-2"><span>→</span> Vaccinating before microchipping (vaccine won't be linked to pet ID)</li>
            <li className="flex gap-2"><span>→</span> Using an expired vaccine certificate</li>
            <li className="flex gap-2"><span>→</span> Not vaccinating at a CDC-approved facility when traveling from high-risk countries</li>
            <li className="flex gap-2"><span>→</span> Missing booster shots for pets with prior vaccinations</li>
          </ul>
        </section>

        <section className="bg-white border border-slate-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-slate-900 mb-3">Related Guides</h2>
          <div className="space-y-2">
            <Link href="/china-to-usa-dog" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ Dog Import: China to USA</Link>
            <Link href="/india-to-usa-dog" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ Dog Import: India to USA</Link>
            <Link href="/cdc-dog-import-rule" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ CDC Dog Import Rule Explained</Link>
          </div>
        </section>
      </div>
    </div>
  );
}
""")

    # ── CDC Dog Import Rule
    write(p("app", "cdc-dog-import-rule", "page.tsx"), """\
import type { Metadata } from 'next';
import Link from 'next/link';

export const metadata: Metadata = {
  title: 'CDC Dog Import Rule – USA Requirements Explained',
  description: 'Full explanation of the CDC dog import rule for bringing dogs into the United States, including the Dog Import Form, CDC-approved facilities, and exemptions.',
  alternates: { canonical: 'https://petentryguide.com/cdc-dog-import-rule' },
};

export default function CDCPage() {
  return (
    <div className="max-w-3xl mx-auto px-4 sm:px-6 py-12">
      <div className="mb-8">
        <div className="inline-flex items-center gap-2 text-xs font-semibold text-brand-600 bg-brand-50 border border-brand-200 rounded-full px-3 py-1 mb-4">🏛️ Rule</div>
        <h1 className="text-3xl font-bold text-slate-900 mb-3">CDC Dog Import Rule</h1>
        <p className="text-slate-500 leading-relaxed">The CDC (Centers for Disease Control and Prevention) regulates the importation of all dogs into the United States. This rule applies to every dog, regardless of origin.</p>
      </div>

      <div className="space-y-8">
        <section className="bg-white border border-slate-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-slate-900 mb-3">What is the CDC Dog Import Form?</h2>
          <p className="text-slate-600 leading-relaxed mb-3">Since August 2024, all dogs entering the USA must have their owner complete the <strong>CDC Dog Import Form</strong> online before travel. Upon submission, you receive a unique <strong>CDC Import Code</strong> via email which must be presented at the port of entry.</p>
          <div className="bg-slate-50 border border-slate-200 rounded-lg p-4 text-sm text-slate-700">
            Submit at: <strong>cdc.gov/importation/dogs</strong>
          </div>
        </section>

        <section className="bg-white border border-slate-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-slate-900 mb-3">High-Risk vs Low-Risk Countries</h2>
          <p className="text-slate-600 text-sm mb-4">The CDC classifies countries as high-risk or low-risk for dog rabies. Dogs from high-risk countries (including China, India, Mexico, and many others) must be vaccinated at a <strong>CDC-approved facility</strong>. Dogs from low-risk countries (UK, EU, Japan, Australia, Canada) follow a simpler process.</p>
          <div className="grid grid-cols-2 gap-4 text-sm">
            <div className="bg-emerald-50 border border-emerald-200 rounded-lg p-4">
              <div className="font-semibold text-emerald-800 mb-2">Low-Risk Countries</div>
              <p className="text-emerald-700">UK, EU, Japan, Australia, Canada, New Zealand, Singapore, South Korea</p>
            </div>
            <div className="bg-amber-50 border border-amber-200 rounded-lg p-4">
              <div className="font-semibold text-amber-800 mb-2">High-Risk Countries</div>
              <p className="text-amber-700">China, India, Mexico, Brazil, and many others — check CDC website for full list</p>
            </div>
          </div>
        </section>

        <section className="bg-amber-50 border border-amber-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-amber-900 mb-3">⚠️ Common Mistakes</h2>
          <ul className="space-y-2 text-amber-800 text-sm">
            <li className="flex gap-2"><span>→</span> Not completing the CDC form before boarding</li>
            <li className="flex gap-2"><span>→</span> Using a non-CDC-approved facility for high-risk countries</li>
            <li className="flex gap-2"><span>→</span> Missing the CDC Import Code at the port of entry</li>
          </ul>
        </section>

        <section className="bg-white border border-slate-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-slate-900 mb-3">Related Guides</h2>
          <div className="space-y-2">
            <Link href="/china-to-usa-dog" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ Dog Import: China to USA</Link>
            <Link href="/india-to-usa-dog" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ Dog Import: India to USA</Link>
            <Link href="/rabies-vaccine-requirements" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ Rabies Vaccine Requirements</Link>
          </div>
        </section>
      </div>
    </div>
  );
}
""")

    # ── USDA Accredited Vet
    write(p("app", "usda-accredited-vet", "page.tsx"), """\
import type { Metadata } from 'next';
import Link from 'next/link';

export const metadata: Metadata = {
  title: 'USDA Accredited Vet – Export Health Certificates Explained',
  description: 'Learn what a USDA-accredited veterinarian is, why you need one for international pet travel, and how to find one.',
  alternates: { canonical: 'https://petentryguide.com/usda-accredited-vet' },
};

export default function USDAPage() {
  return (
    <div className="max-w-3xl mx-auto px-4 sm:px-6 py-12">
      <div className="mb-8">
        <div className="inline-flex items-center gap-2 text-xs font-semibold text-brand-600 bg-brand-50 border border-brand-200 rounded-full px-3 py-1 mb-4">🩺 Rule</div>
        <h1 className="text-3xl font-bold text-slate-900 mb-3">USDA Accredited Vet</h1>
        <p className="text-slate-500 leading-relaxed">When exporting a pet from the United States, or when destination countries require it, you need an Export Health Certificate (EHC) signed by a USDA-accredited veterinarian and endorsed by the USDA APHIS.</p>
      </div>

      <div className="space-y-8">
        <section className="bg-white border border-slate-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-slate-900 mb-3">What is a USDA-Accredited Vet?</h2>
          <p className="text-slate-600 leading-relaxed">A USDA-accredited veterinarian is a private veterinarian authorized by the USDA Animal and Plant Health Inspection Service (APHIS) to certify animals for interstate and international travel. Not all vets are accredited — you must specifically seek one with USDA accreditation.</p>
        </section>

        <section className="bg-white border border-slate-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-slate-900 mb-3">When Do You Need One?</h2>
          <ul className="space-y-2 text-slate-600 text-sm">
            <li className="flex gap-2"><span className="text-brand-500">→</span> Exporting a pet from the USA to another country</li>
            <li className="flex gap-2"><span className="text-brand-500">→</span> Certain destination countries require USDA-backed health certificates</li>
            <li className="flex gap-2"><span className="text-brand-500">→</span> Getting a certificate endorsed by USDA APHIS (required by many countries)</li>
          </ul>
        </section>

        <section className="bg-white border border-slate-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-slate-900 mb-3">How to Find a USDA-Accredited Vet</h2>
          <p className="text-slate-600 text-sm leading-relaxed mb-3">Visit the USDA APHIS website and use the Accredited Vet search tool. Search by state and zip code. Always call ahead to confirm the vet is familiar with international health certificate requirements.</p>
          <div className="bg-slate-50 border border-slate-200 rounded-lg p-4 text-sm text-slate-700">
            Search at: <strong>aphis.usda.gov</strong> → Veterinary Accreditation
          </div>
        </section>

        <section className="bg-white border border-slate-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-slate-900 mb-3">Related Guides</h2>
          <div className="space-y-2">
            <Link href="/pet-travel-checklist" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ Pet Travel Checklist</Link>
            <Link href="/cdc-dog-import-rule" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ CDC Dog Import Rule</Link>
          </div>
        </section>
      </div>
    </div>
  );
}
""")

    # ── Pet Travel Checklist
    write(p("app", "pet-travel-checklist", "page.tsx"), """\
import type { Metadata } from 'next';
import Link from 'next/link';

export const metadata: Metadata = {
  title: 'Pet Travel Checklist – Complete International Travel Prep Guide',
  description: 'A complete checklist for traveling internationally with your pet. Documents, vaccinations, airline preparation, and arrival tips.',
  alternates: { canonical: 'https://petentryguide.com/pet-travel-checklist' },
};

export default function ChecklistPage() {
  const sections = [
    {
      title: '3–6 Months Before Travel',
      emoji: '📅',
      items: [
        'Research destination country pet import requirements',
        'Ensure microchip is ISO 11784/85 compatible',
        'Microchip the pet if not already done',
        'Schedule rabies vaccination (after microchipping)',
        'Find a USDA-accredited vet or equivalent in your country',
        'Research airline pet policies and book pet-friendly flight',
      ]
    },
    {
      title: '1–2 Months Before Travel',
      emoji: '📆',
      items: [
        'Obtain Export Health Certificate from accredited vet',
        'Have certificate endorsed by government veterinary authority',
        'Complete CDC Dog Import Form (for USA entry with dogs)',
        'Purchase IATA-compliant pet carrier or crate',
        'Begin crate training if traveling in cargo',
        'Schedule vet check-up to confirm pet is fit to fly',
      ]
    },
    {
      title: '1–2 Weeks Before Travel',
      emoji: '🗓️',
      items: [
        'Confirm health certificate is within validity period (usually 10 days)',
        'Print all documents (health certificate, vaccination records, CDC form)',
        'Confirm CDC Import Code has been received via email',
        'Purchase travel-size food, water bowl, and comfort items',
        'Inform airline of pet as baggage/cargo if not already done',
      ]
    },
    {
      title: 'Day of Travel',
      emoji: '✈️',
      items: [
        'Arrive at airport 3 hours early (more for cargo pets)',
        'Bring all original documents (not just copies)',
        'Show CDC Import Code at check-in if required',
        'Avoid feeding pet 4–6 hours before flight',
        'Attach water and food to crate for cargo flights',
        'Label crate with contact information',
      ]
    },
    {
      title: 'Upon Arrival',
      emoji: '🏁',
      items: [
        'Proceed to customs and declare your pet',
        'Present health certificate and vaccination records',
        'Present CDC Import Code (for USA dog entry)',
        'Allow extra time for inspection if required',
        'Check pet for stress signs after travel',
        'Consult a local vet within 48 hours if needed',
      ]
    },
  ];

  return (
    <div className="max-w-3xl mx-auto px-4 sm:px-6 py-12">
      <div className="mb-10">
        <div className="inline-flex items-center gap-2 text-xs font-semibold text-brand-600 bg-brand-50 border border-brand-200 rounded-full px-3 py-1 mb-4">📋 Practical Guide</div>
        <h1 className="text-3xl font-bold text-slate-900 mb-3">Pet Travel Checklist</h1>
        <p className="text-slate-500 leading-relaxed">Use this step-by-step checklist to prepare for international travel with your pet. Start 3–6 months before your departure date.</p>
      </div>

      <div className="space-y-6">
        {sections.map((section) => (
          <div key={section.title} className="bg-white border border-slate-200 rounded-xl p-6">
            <h2 className="text-base font-bold text-slate-900 mb-4 flex items-center gap-2">
              <span>{section.emoji}</span> {section.title}
            </h2>
            <ul className="space-y-2">
              {section.items.map((item, i) => (
                <li key={i} className="flex items-start gap-3 text-sm text-slate-700">
                  <span className="w-4 h-4 border-2 border-slate-300 rounded flex-shrink-0 mt-0.5"></span>
                  {item}
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>

      <div className="mt-10 bg-brand-50 border border-brand-200 rounded-xl p-6">
        <h2 className="font-bold text-brand-900 mb-3">Related Guides</h2>
        <div className="space-y-2">
          <Link href="/cost-to-bring-cat-to-usa" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ Cost to Bring a Cat to USA</Link>
          <Link href="/pet-cargo-travel-guide" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ Pet Cargo Travel Guide</Link>
          <Link href="/rabies-vaccine-requirements" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ Rabies Vaccine Requirements</Link>
        </div>
      </div>
    </div>
  );
}
""")

    # ── Cost to Bring Cat to USA
    write(p("app", "cost-to-bring-cat-to-usa", "page.tsx"), """\
import type { Metadata } from 'next';
import Link from 'next/link';

export const metadata: Metadata = {
  title: 'Cost to Bring a Cat to the USA – 2026 Breakdown',
  description: 'Complete cost breakdown for bringing a cat to the United States from any country: vet fees, airline fees, health certificates, and more.',
  alternates: { canonical: 'https://petentryguide.com/cost-to-bring-cat-to-usa' },
};

export default function CostPage() {
  const costs = [
    { item: 'ISO Microchip (if needed)', low: 30, high: 80 },
    { item: 'Rabies Vaccination', low: 20, high: 100 },
    { item: 'Export Health Certificate (Vet Fee)', low: 100, high: 350 },
    { item: 'Government Endorsement Fee', low: 30, high: 150 },
    { item: 'Airline Pet-in-Cabin Fee', low: 95, high: 200 },
    { item: 'Airline Cargo Fee', low: 200, high: 600 },
    { item: 'IATA-compliant Carrier/Crate', low: 40, high: 200 },
    { item: 'Pet Relocation Service (optional)', low: 500, high: 3000 },
  ];

  const totalLow  = costs.reduce((s, c) => s + c.low, 0);
  const totalHigh = costs.reduce((s, c) => s + c.high, 0);

  return (
    <div className="max-w-3xl mx-auto px-4 sm:px-6 py-12">
      <div className="mb-10">
        <div className="inline-flex items-center gap-2 text-xs font-semibold text-brand-600 bg-brand-50 border border-brand-200 rounded-full px-3 py-1 mb-4">💰 Practical Guide</div>
        <h1 className="text-3xl font-bold text-slate-900 mb-3">Cost to Bring a Cat to the USA</h1>
        <p className="text-slate-500 leading-relaxed">Bringing a cat to the USA involves multiple fees. Here is a comprehensive 2026 cost breakdown to help you budget for your pet's international move.</p>
      </div>

      <div className="bg-white border border-slate-200 rounded-xl overflow-hidden mb-8">
        <table className="w-full text-sm">
          <thead>
            <tr className="bg-slate-50 border-b border-slate-200">
              <th className="text-left px-5 py-3 font-semibold text-slate-600">Item</th>
              <th className="text-right px-5 py-3 font-semibold text-slate-600">Low (USD)</th>
              <th className="text-right px-5 py-3 font-semibold text-slate-600">High (USD)</th>
            </tr>
          </thead>
          <tbody>
            {costs.map((c, i) => (
              <tr key={i} className="border-b border-slate-100 hover:bg-slate-50">
                <td className="px-5 py-3 text-slate-700">{c.item}</td>
                <td className="px-5 py-3 text-right text-slate-700">${c.low}</td>
                <td className="px-5 py-3 text-right text-slate-700">${c.high}</td>
              </tr>
            ))}
            <tr className="bg-brand-50 font-bold">
              <td className="px-5 py-3 text-brand-900">Estimated Total</td>
              <td className="px-5 py-3 text-right text-brand-900">${totalLow.toLocaleString()}</td>
              <td className="px-5 py-3 text-right text-brand-900">${totalHigh.toLocaleString()}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div className="bg-amber-50 border border-amber-200 rounded-xl p-6 mb-8">
        <h2 className="font-bold text-amber-900 mb-2">💡 Tips to Reduce Costs</h2>
        <ul className="space-y-2 text-amber-800 text-sm">
          <li className="flex gap-2"><span>→</span> Book flights directly with airlines that allow pets in cabin (avoid cargo fees)</li>
          <li className="flex gap-2"><span>→</span> Use a USDA-accredited vet for the health certificate to avoid rebooking fees</li>
          <li className="flex gap-2"><span>→</span> Prepare all documents yourself instead of using a full relocation service</li>
        </ul>
      </div>

      <div className="bg-white border border-slate-200 rounded-xl p-6">
        <h2 className="font-bold text-slate-900 mb-3">Related Guides</h2>
        <div className="space-y-2">
          <Link href="/china-to-usa-cat" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ Cat Import: China to USA</Link>
          <Link href="/pet-travel-checklist" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ Pet Travel Checklist</Link>
          <Link href="/pet-cargo-travel-guide" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ Pet Cargo Travel Guide</Link>
        </div>
      </div>
    </div>
  );
}
""")

    # ── Pet Cargo Travel Guide
    write(p("app", "pet-cargo-travel-guide", "page.tsx"), """\
import type { Metadata } from 'next';
import Link from 'next/link';

export const metadata: Metadata = {
  title: 'Pet Cargo Travel Guide – How to Ship Your Pet Safely',
  description: 'Everything you need to know about shipping your pet as cargo on international flights: crate requirements, airline policies, preparation tips, and arrival.',
  alternates: { canonical: 'https://petentryguide.com/pet-cargo-travel-guide' },
};

export default function CargoPage() {
  return (
    <div className="max-w-3xl mx-auto px-4 sm:px-6 py-12">
      <div className="mb-10">
        <div className="inline-flex items-center gap-2 text-xs font-semibold text-brand-600 bg-brand-50 border border-brand-200 rounded-full px-3 py-1 mb-4">✈️ Practical Guide</div>
        <h1 className="text-3xl font-bold text-slate-900 mb-3">Pet Cargo Travel Guide</h1>
        <p className="text-slate-500 leading-relaxed">For large pets, long-haul flights, or airlines that don't allow cabin pets, cargo is the standard option. This guide covers everything you need to prepare for safe cargo travel.</p>
      </div>

      <div className="space-y-8">
        <section className="bg-white border border-slate-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-slate-900 mb-3">IATA Crate Requirements</h2>
          <p className="text-slate-600 text-sm mb-4">All cargo pets must travel in an <strong>IATA Live Animal Regulations</strong>-compliant crate. Requirements include:</p>
          <ul className="space-y-2 text-slate-600 text-sm">
            <li className="flex gap-2"><span className="text-brand-500">→</span> Rigid walls with proper ventilation on at least 3 sides</li>
            <li className="flex gap-2"><span className="text-brand-500">→</span> Pet must be able to stand, turn around, and lie down naturally</li>
            <li className="flex gap-2"><span className="text-brand-500">→</span> Water and food containers accessible from outside</li>
            <li className="flex gap-2"><span className="text-brand-500">→</span> "Live Animal" labels on top and sides</li>
            <li className="flex gap-2"><span className="text-brand-500">→</span> Absorbent bedding inside</li>
          </ul>
        </section>

        <section className="bg-white border border-slate-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-slate-900 mb-3">How to Prepare Your Pet</h2>
          <ul className="space-y-2 text-slate-600 text-sm">
            <li className="flex gap-2"><span className="text-emerald-500">✓</span> Begin crate training 4–6 weeks before travel</li>
            <li className="flex gap-2"><span className="text-emerald-500">✓</span> Fast the pet 4–6 hours before the flight</li>
            <li className="flex gap-2"><span className="text-emerald-500">✓</span> Exercise the pet well before drop-off</li>
            <li className="flex gap-2"><span className="text-emerald-500">✓</span> Do NOT sedate pets for air travel (increases health risk)</li>
            <li className="flex gap-2"><span className="text-emerald-500">✓</span> Attach a familiar item (blanket, toy) for comfort</li>
          </ul>
        </section>

        <section className="bg-amber-50 border border-amber-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-amber-900 mb-3">⚠️ Important Warnings</h2>
          <ul className="space-y-2 text-amber-800 text-sm">
            <li className="flex gap-2"><span>→</span> Many airlines embargo cargo pets during extreme temperatures</li>
            <li className="flex gap-2"><span>→</span> Snub-nosed breeds (bulldogs, persians) are often restricted from cargo</li>
            <li className="flex gap-2"><span>→</span> Cargo is temperature-controlled but not identical to cabin conditions</li>
          </ul>
        </section>

        <section className="bg-white border border-slate-200 rounded-xl p-6">
          <h2 className="text-lg font-bold text-slate-900 mb-3">Related Guides</h2>
          <div className="space-y-2">
            <Link href="/pet-travel-checklist" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ Pet Travel Checklist</Link>
            <Link href="/cost-to-bring-cat-to-usa" className="flex items-center gap-2 text-brand-600 hover:underline text-sm">→ Cost to Bring a Cat to USA</Link>
          </div>
        </section>
      </div>
    </div>
  );
}
""")


# ─────────────────────────────────────────────
# SITEMAP
# ─────────────────────────────────────────────

def gen_sitemap():
    print("\n[9/9] Writing sitemap.ts...")
    slugs_str = "\n".join([f"    '{r['slug']}'," for r in ROUTES])
    write(p("app", "sitemap.ts"), f"""\
import {{ MetadataRoute }} from 'next';

const BASE_URL = 'https://petentryguide.com';

const ROUTE_SLUGS = [
{slugs_str}
];

const STATIC_PAGES = [
  '/rabies-vaccine-requirements',
  '/cdc-dog-import-rule',
  '/usda-accredited-vet',
  '/pet-travel-checklist',
  '/cost-to-bring-cat-to-usa',
  '/pet-cargo-travel-guide',
];

export default function sitemap(): MetadataRoute.Sitemap {{
  const routes = ROUTE_SLUGS.map(slug => ({{
    url: `${{BASE_URL}}/${{slug}}`,
    lastModified: new Date(),
    changeFrequency: 'monthly' as const,
    priority: 0.8,
  }}));

  const staticPages = STATIC_PAGES.map(path => ({{
    url: `${{BASE_URL}}${{path}}`,
    lastModified: new Date(),
    changeFrequency: 'monthly' as const,
    priority: 0.6,
  }}));

  return [
    {{ url: BASE_URL, lastModified: new Date(), changeFrequency: 'weekly', priority: 1 }},
    ...routes,
    ...staticPages,
  ];
}}
""")


# ─────────────────────────────────────────────
# README
# ─────────────────────────────────────────────

def gen_readme():
    write(p("README.md"), f"""\
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
/data/routes      – JSON data for {len(ROUTES)} route guides
/lib              – getRoutes.ts data helpers
```

## Routes Generated

{chr(10).join(f'- /{r["slug"]}' for r in ROUTES)}

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
""")


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    print(f"\n🐾 PetEntryGuide Site Generator")
    print(f"   Output directory: ./{BASE_DIR}/")
    print(f"   Routes: {len(ROUTES)}")

    os.makedirs(BASE_DIR, exist_ok=True)

    gen_data()
    gen_package_json()
    gen_lib()
    gen_components()
    gen_app_shell()
    gen_home()
    gen_slug_page()
    gen_static_pages()
    gen_sitemap()
    gen_readme()

    print(f"\n✅ Done! Generated {len(ROUTES)} route guides.")
    print(f"\nNext steps:")
    print(f"  cd {BASE_DIR}")
    print(f"  npm install")
    print(f"  npm run dev")


if __name__ == "__main__":
    main()
