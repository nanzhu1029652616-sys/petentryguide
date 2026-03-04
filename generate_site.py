import csv
import os
from datetime import date

SITE = "https://petentryguide.com"
TODAY = date.today().isoformat()

# 导航链接
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
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }}
    h1 {{ color: #1a73e8; border-bottom: 2px solid #eee; padding-bottom: 10px; }}
    .content {{ background: #f9f9f9; padding: 20px; border-radius: 8px; border: 1px solid #eee; margin: 20px 0; }}
    .footer {{ margin-top: 40px; font-size: 0.9em; color: #666; border-top: 1px solid #eee; padding-top: 20px; }}
    li {{ margin-bottom: 8px; }}
</style>
</head>
<body>

<h1>{title}</h1>
<p><em>Last updated: {today}</em></p>

<div class="content">
{article_body}
</div>

<h2>Essential Preparation</h2>
<ul>
    <li>ISO 11784/11785 compliant microchip</li>
    <li>Rabies vaccination (at least 30 days before travel)</li>
    <li>International health certificate (endorsed by local authorities)</li>
    <li>IATA approved travel crate</li>
</ul>

<h2>Related Guides</h2>
<ul>
{related_links}
</ul>

<div class="footer">
    <p>© {year} Pet Entry Guide - Expert assistance for your pet's relocation to the USA.</p>
</div>

</body>
</html>
"""

SITEMAP_HEADER = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""
SITEMAP_FOOTER = "</urlset>\n"

def slug_to_path(slug: str) -> str:
    return f"/{slug}"

def make_desc(title: str) -> str:
    return f"Complete 2026 requirements for {title}. Learn about microchips, vaccines, and documentation."

def ensure_topics():
    if not os.path.exists("topics.csv"):
        raise FileNotFoundError("topics.csv not found.")

def read_topics():
    topics = []
    with open("topics.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            slug = (row.get("slug") or "").strip()
            title = (row.get("title") or "").strip()
            # 获取内容列，如果没有这一列或内容为空，设为 None
            content = row.get("content", "").strip()
            if not slug or not title:
                continue
            topics.append((slug, title, content))
    return topics

def write_page(slug: str, title: str, content: str):
    path = slug_to_path(slug)
    canonical = f"{SITE}{path}"
    related = "\n".join([f'    <li><a href="{href}">{text}</a></li>' for href, text in NAV_LINKS])

    # 如果 content 为空，生成默认段落
    article_body = content if content else f"<p>Bringing your pet to the United States involves several critical steps. For <strong>{title}</strong>, you must ensure all vaccinations are up to date and all documents are endorsed by the proper government agencies. This guide covers the essential timeline and requirements for a smooth arrival.</p>"

    html = PAGE_TEMPLATE.format(
        title=title,
        desc=make_desc(title),
        canonical=canonical,
        today=TODAY,
        article_body=article_body,
        related_links=related,
        year=str(date.today().year)
    )

    filename = f"{slug}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

def write_index(topics):
    links = "\n".join([f'    <li><a href="{slug_to_path(slug)}">{title}</a></li>' for slug, title, content in topics])
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Pet Entry Guide | USA Pet Import 2026</title>
  <style>body{{font-family:sans-serif; line-height:1.6; max-width:800px; margin:0 auto; padding:20px;}} a{{color:#1a73e8;}}</style>
</head>
<body>
  <h1>Pet Entry Guide</h1>
  <p>Find the specific requirements for your pet's journey to the USA:</p>
  <ul>{links}</ul>
</body>
</html>"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

def write_sitemap(topics):
    items = [f"<url><loc>{SITE}/</loc><lastmod>{TODAY}</lastmod><priority>1.0</priority></url>"]
    for slug, _, _ in topics:
        items.append(f"<url><loc>{SITE}/{slug}</loc><lastmod>{TODAY}</lastmod><priority>0.8</priority></url>")
    xml = SITEMAP_HEADER + "\n".join(items) + SITEMAP_FOOTER
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(xml)

def main():
    ensure_topics()
    topics = read_topics()
    for slug, title, content in topics:
        write_page(slug, title, content)
    write_index(topics)
    write_sitemap(topics)
    print(f"Success! Processed {len(topics)} pages.")

if __name__ == "__main__":
    main()
