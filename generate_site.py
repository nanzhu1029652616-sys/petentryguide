import csv
import os
from datetime import date

SITE = "https://petentryguide.com"
TODAY = date.today().isoformat()

# 你想要的内部链接（每篇文章底部都会放）
NAV_LINKS = [
    ("/usa-pet-import", "USA Pet Import Guide"),
    ("/pet-travel-documents-checklist", "Pet Documents Checklist"),
    ("/pet-travel-cost-usa", "Cost to Bring a Pet to the USA"),
]

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title} | Pet Entry Guide</title>
<meta name="description" content="Complete guide: {title}. Requirements, documents, timeline and costs.">
</head>

<body>

<h1>{title}</h1>

<p>This guide explains everything you need to know about {title.lower()}.</p>

<h2>Requirements</h2>

<ul>
<li>ISO compatible microchip</li>
<li>Rabies vaccination</li>
<li>Veterinary health certificate</li>
<li>Airline approved pet crate</li>
</ul>

<h2>Step-by-Step Process</h2>

<ol>
<li>Microchip your pet</li>
<li>Get rabies vaccination</li>
<li>Prepare health certificate</li>
<li>Book airline pet travel</li>
<li>Prepare travel crate</li>
</ol>

<h2>Estimated Cost</h2>

<p>The cost of bringing a pet to the United States typically ranges from $800 to $4000 depending on airline, distance, and whether you use a relocation service.</p>

<h2>Timeline</h2>

<p>Most pet import preparation takes 1–3 months depending on vaccination timing and documentation.</p>

<h2>FAQ</h2>

<h3>Do pets need quarantine in the United States?</h3>
<p>Most pets do not need quarantine if documentation and vaccinations are correct.</p>

<h3>Can pets travel in cabin?</h3>
<p>Many airlines allow small pets in cabin if they meet carrier size requirements.</p>

<h2>Related Guides</h2>

<ul>
<li><a href="/usa-pet-import">USA Pet Import Rules</a></li>
<li><a href="/pet-travel-cost-usa">Pet Travel Cost Guide</a></li>
<li><a href="/pet-health-certificate">Pet Health Certificate Guide</a></li>
</ul>

</body>
</html>
"""

SITEMAP_HEADER = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""
SITEMAP_FOOTER = "</urlset>\n"

def slug_to_path(slug: str) -> str:
    # 你的站现在是“干净URL”，访问 /slug（不带 .html）
    return f"/{slug}"

def make_desc(title: str) -> str:
    return f"{title}. Requirements, documents, timeline, airline tips, and common mistakes."

def make_intro(title: str) -> str:
    return f"This page summarizes the key requirements and practical steps related to: {title}."

def ensure_topics():
    if not os.path.exists("topics.csv"):
        raise FileNotFoundError("topics.csv not found in repo root.")

def read_topics():
    topics = []
    with open("topics.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            slug = (row.get("slug") or "").strip()
            title = (row.get("title") or "").strip()
            if not slug or not title:
                continue
            topics.append((slug, title))
    if not topics:
        raise ValueError("No topics found in topics.csv")
    return topics

def write_page(slug: str, title: str):
    path = slug_to_path(slug)
    canonical = f"{SITE}{path}"
    related = "\n      ".join([f'<li><a href="{href}">{text}</a></li>' for href, text in NAV_LINKS])

    html = PAGE_TEMPLATE.format(
        title=title,
        desc=make_desc(title),
        canonical=canonical,
        today=TODAY,
        intro=make_intro(title),
        related_links=related,
        year=str(date.today().year),
    )

    filename = f"{slug}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

def write_index(topics):
    links = "\n".join([f'<li><a href="{slug_to_path(slug)}">{title}</a></li>' for slug, title in topics])
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Pet Entry Guide</title>
  <meta name="description" content="Practical guides for pet import rules, documents, costs, and airline travel." />
  <link rel="canonical" href="{SITE}/" />
</head>
<body>
  <h1>Pet Entry Guide</h1>
  <p><em>Last updated: {TODAY}</em></p>
  <p>Browse guides:</p>
  <ul>
    {links}
  </ul>
</body>
</html>
"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

def write_sitemap(topics):
    items = []
    # 首页
    items.append(f"""<url>
  <loc>{SITE}/</loc>
  <lastmod>{TODAY}</lastmod>
  <changefreq>weekly</changefreq>
  <priority>1.0</priority>
</url>
""")
    # 每个页面
    for slug, _title in topics:
        url = f"{SITE}{slug_to_path(slug)}"
        items.append(f"""<url>
  <loc>{url}</loc>
  <lastmod>{TODAY}</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.8</priority>
</url>
""")
    xml = SITEMAP_HEADER + "\n".join(items) + SITEMAP_FOOTER
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(xml)

def main():
    ensure_topics()
    topics = read_topics()

    # 生成所有页面
    for slug, title in topics:
        write_page(slug, title)

    # 生成首页目录 + sitemap
    write_index(topics)
    write_sitemap(topics)

    print(f"Done. Generated {len(topics)} pages, plus index.html and sitemap.xml")

if __name__ == "__main__":
    main()
