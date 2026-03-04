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

# 专门为首页设计的模板
INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pet Entry Guide | 2026 International Pet Travel Portal</title>
<style>
    :root {{ --primary: #1a73e8; --text: #202124; --bg: #f8f9fa; }}
    body {{ 
        font-family: 'Inter', -apple-system, sans-serif; 
        line-height: 1.6; color: var(--text); background: var(--bg);
        margin: 0; padding: 0; 
    }}
    .hero {{ 
        background: white; border-bottom: 1px solid #dadce0; 
        padding: 60px 20px; text-align: center; 
    }}
    .hero h1 {{ font-size: 2.8em; margin-bottom: 10px; letter-spacing: -0.03em; }}
    .hero p {{ color: #70757a; font-size: 1.2em; max-width: 600px; margin: 0 auto; }}
    
    .container {{ max-width: 1100px; margin: 40px auto; padding: 0 20px; }}
    
    /* 网格布局 */
    .grid {{ 
        display: grid; 
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); 
        gap: 20px; 
    }}
    
    /* 卡片样式 */
    .card {{ 
        background: white; border: 1px solid #dadce0; border-radius: 12px; 
        padding: 24px; transition: all 0.2s; text-decoration: none; color: inherit;
        display: flex; flex-direction: column;
    }}
    .card:hover {{ 
        border-color: var(--primary); box-shadow: 0 4px 12px rgba(26,115,232,0.1); 
        transform: translateY(-2px);
    }}
    .card h3 {{ margin: 0 0 10px 0; color: var(--primary); font-size: 1.25em; }}
    .card p {{ margin: 0; font-size: 0.9em; color: #5f6368; }}
    
    .footer {{ text-align: center; padding: 40px; color: #70757a; font-size: 0.9em; }}
</style>
</head>
<body>

<div class="hero">
    <h1>Pet Entry Guide</h1>
    <p>Find specific requirements and expert relocation guides for your pet's journey to the USA (2026 Updated).</p>
</div>

<div class="container">
    <div class="grid">
        {index_items}
    </div>
</div>

<div class="footer">
    <p>© 2026 Pet Entry Guide. High-quality data for responsible pet owners.</p>
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
