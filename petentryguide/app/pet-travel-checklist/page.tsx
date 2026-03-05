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
