import csv
import os
from datetime import datetime

# 1. 文章详情页模板
PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>[[TITLE]] | Pet Entry Guide</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lipis/flag-icons@7.0.0/css/flag-icons.min.css"/>
<style>
    :root { --primary: #1a73e8; --text: #202124; --bg: #ffffff; }
    body { font-family: 'Inter', sans-serif; line-height: 1.7; color: var(--text); max-width: 800px; margin: 0 auto; padding: 40px 20px; }
    .back-home { margin-bottom: 20px; display: inline-block; text-decoration: none; color: var(--primary); font-weight: 500; }
    h1 { font-size: 2.5em; margin-bottom: 10px; }
    .meta { font-size: 0.9em; color: #70757a; margin-bottom: 30px; border-bottom: 1px solid #eee; padding-bottom: 10px; }
    .content strong { color: var(--primary); background: #e8f0fe; padding: 2px 6px; border-radius: 4px; }
    .footer { margin-top: 80px; font-size: 0.85em; color: #70757a; text-align: center; border-top: 1px solid #eee; padding-top: 30px; }
</style>
</head>
<body>
    <a href="/" class="back-home">← Back to Portal</a>
    <h1>[[TITLE]]</h1>
    <p class="meta">Expert Relocation Guide • Updated [[TODAY]]</p>
    <div class="content">[[BODY]]</div>
    <div class="footer"><p>© 2026 Pet Entry Guide. Information based on current 2026 travel regulations.</p></div>
</body>
</html>
"""

# 2. 首页门户模板
INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pet Entry Guide | 2026 USA Pet Travel Portal</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lipis/flag-icons@7.0.0/css/flag-icons.min.css"/>
<style>
    :root { --primary: #1a73e8; --text: #202124; --bg: #f8f9fa; }
    body { font-family: 'Inter', sans-serif; line-height: 1.6; color: var(--text); background: var(--bg); margin: 0; }
    .hero { background: white; border-bottom: 1px solid #dadce0; padding: 60px 20px; text-align: center; }
    .hero h1 { font-size: 3.2em; color: #1a0dab; margin-bottom: 10px; }
    .search-container { margin: 30px auto; max-width: 500px; position: relative; }
    #search-input { width: 100%; padding: 15px 45px; border: 1px solid #dadce0; border-radius: 30px; font-size: 1.1em; box-shadow: 0 1px 6px rgba(32,33,36,0.1); outline: none; box-sizing: border-box; }
    .nav-tags { display: flex; justify-content: center; flex-wrap: wrap; gap: 10px; margin: 20px auto; max-width: 1000px; }
    .tag { background: white; border: 1px solid #dadce0; padding: 8px 16px; border-radius: 20px; text-decoration: none; color: #5f6368; font-size: 0.9em; transition: 0.2s; display: flex; align-items: center; }
    .tag:hover { border-color: var(--primary); color: var(--primary); }
    .container { max-width: 1200px; margin: 0 auto; padding: 0 25px; }
    .section-title { font-size: 1.8em; margin: 50px 0 25px; display: flex; align-items: center; border-left: 5px solid var(--primary); padding-left: 15px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 25px; }
    .card { background: white; border: 1px solid #dadce0; border-radius: 16px; padding: 25px; text-decoration: none; color: inherit; display: flex; flex-direction: column; transition: 0.3s; }
    .card:hover { border-color: var(--primary); box-shadow: 0 10px 25px rgba(26,115,232,0.1); transform: translateY(-3px); }
    .card h3 { margin: 0 0 10px 0; color: var(--primary); }
    .card p { margin: 0; font-size: 0.9em; color: #5f6368; overflow: hidden; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; }
    #no-results { text-align: center; padding: 50px; display: none; color: #70757a; }
</style>
</head>
<body>
<div class="hero">
    <h1>Pet Entry Guide</h1>
    <div class="search-container">
        <input type="text" id="search-input" placeholder="Search guides (e.g., 'China', 'fees')...">
    </div>
    <div class="nav-tags">[[NAV_TAGS]]</div>
</div>
<div class="container" id="main-content">
    [[CONTENT_SECTIONS]]
    <div id="no-results">No guides found matching your search.</div>
</div>

<script>
    const searchInput = document.getElementById('search-input');
    const cards = document.querySelectorAll('.card');
    const titles = document.querySelectorAll('.section-title');
    const noResults = document.getElementById('no-results');

    searchInput.addEventListener('input', (e) => {
        const term = e.target.value.toLowerCase();
        let foundAny = false;

        titles.forEach((title, idx) => {
            const grid = title.nextElementSibling;
            let foundInGrid = false;
            grid.querySelectorAll('.card').forEach(card => {
                const match = card.innerText.toLowerCase().includes(term);
                card.style.display = match ? 'flex' : 'none';
                if (match) { foundInGrid = foundAny = true; }
            });
            title.style.display = foundInGrid ? 'flex' : 'none';
            grid.style.display = foundInGrid ? 'grid' : 'none';
        });
        noResults.style.display = foundAny ? 'none' : 'block';
    });
</script>
</body>
</html>
"""

def main():
    country_map = {
        'china': {'name': 'China', 'code': 'cn'}, 'japan': {'name': 'Japan', 'code': 'jp'},
        'korea': {'name': 'South Korea', 'code': 'kr'}, 'singapore': {'name': 'Singapore', 'code': 'sg'},
        'australia': {'name': 'Australia', 'code': 'au'}, 'canada': {'name': 'Canada', 'code': 'ca'},
        'uk': {'name': 'United Kingdom', 'code': 'gb'}, 'eu': {'name': 'Europe', 'code': 'eu'},
        'mexico': {'name': 'Mexico', 'code': 'mx'}, 'usa': {'name': 'USA General', 'code': 'us'}
    }

    if not os.path.exists('topics.csv'): return
    with open('topics.csv', 'r', encoding='utf-8') as f:
        rows = list(csv.reader(f))[1:]
        rows = [r for r in rows if len(r) >= 2 and r[0].strip()]

    today = datetime.now().strftime('%b %d, %Y')
    grouped = {}
    for slug, title, content in rows:
        c_key = slug.split('-')[0]
        info = country_map.get(c_key, {'name': 'Other Guides', 'code': 'us'})
        if info['name'] not in grouped: grouped[info['name']] = {'code': info['code'], 'items': []}
        grouped[info['name']]['items'].append({'slug': slug, 'title': title, 'content': content})

        # 生成详情页
        page_html = PAGE_TEMPLATE.replace('[[TITLE]]', title).replace('[[TODAY]]', today).replace('[[BODY]]', content)
        with open(f"{slug}.html", 'w', encoding='utf-8') as f_out: f_out.write(page_html)

    nav_tags, content_sections = "", ""
    for country in sorted(grouped.keys()):
        code = grouped[country]['code']
        nav_tags += f'<a href="#{country}" class="tag"><span class="fi fi-{code}"></span>&nbsp;{country}</a>'
        content_sections += f'<h2 class="section-title" id="{country}"><span class="fi fi-{code}"></span>&nbsp;{country}</h2><div class="grid">'
        for item in grouped[country]['items']:
            snippet = item['content'].replace('<p>', '').replace('</p>', '')[:120] + "..."
            content_sections += f'<a href="{item["slug"]}.html" class="card"><h3>{item["title"]}</h3><p>{snippet}</p></a>'
        content_sections += '</div>'

    index_html = INDEX_TEMPLATE.replace('[[NAV_TAGS]]', nav_tags).replace('[[CONTENT_SECTIONS]]', content_sections)
    with open('index.html', 'w', encoding='utf-8') as f_idx: f_idx.write(index_html)
    print(f"Success! Processed {len(rows)} pages.")

if __name__ == "__main__":
    import csv
    main()
