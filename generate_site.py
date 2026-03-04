import csv
import os
from datetime import datetime

# 1. 详情页模板：强化“操作指引”
PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>[[TITLE]] | 2026 Pet Travel Expert</title>
<style>
    :root { --primary: #1a73e8; --text: #202124; --bg: #ffffff; --breadcrumb: #5f6368; }
    body { font-family: 'Inter', -apple-system, sans-serif; line-height: 1.7; color: var(--text); margin: 0; background: var(--bg); }
    .nav { border-bottom: 1px solid #eee; padding: 15px 20px; background: white; position: sticky; top: 0; z-index: 100; }
    .nav-inner { max-width: 900px; margin: 0 auto; font-size: 0.9em; }
    .nav a { color: var(--breadcrumb); text-decoration: none; }
    .container { max-width: 800px; margin: 40px auto; padding: 0 20px; }
    h1 { font-size: 2.6em; letter-spacing: -0.02em; line-height: 1.2; margin-bottom: 10px; }
    .status-badge { display: inline-block; background: #ceead6; color: #0d652d; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-bottom: 20px; }
    .content { font-size: 1.15em; border-top: 1px solid #eee; padding-top: 30px; }
    .content strong { color: var(--primary); background: #e8f0fe; padding: 2px 5px; border-radius: 4px; }
    .footer { margin-top: 100px; padding: 40px; text-align: center; background: #f8f9fa; color: #70757a; font-size: 0.9em; }
</style>
</head>
<body>
    <div class="nav"><div class="nav-inner"><a href="/">Home</a> / <a href="/#[[COUNTRY_ID]]">[[COUNTRY_NAME]]</a> / [[TITLE]]</div></div>
    <div class="container">
        <div class="status-badge">● 2026 Regulations Active</div>
        <h1>[[TITLE]]</h1>
        <div class="content">[[BODY]]</div>
    </div>
    <div class="footer">© 2026 Pet Entry Guide. Verified by Relocation Experts.</div>
</body>
</html>
"""

# 2. 首页模板：专业、高效、透明
INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pet Entry Guide | 2026 International Pet Relocation Portal</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lipis/flag-icons@7.0.0/css/flag-icons.min.css"/>
<style>
    :root { --primary: #1a73e8; --bg: #f8f9fa; --card: #ffffff; }
    body { font-family: 'Inter', sans-serif; color: #202124; background: var(--bg); margin: 0; }
    .hero { background: white; padding: 80px 20px; text-align: center; border-bottom: 1px solid #dadce0; }
    h1 { font-size: 3.5em; letter-spacing: -0.04em; color: #1a0dab; margin-bottom: 15px; }
    .search-box { max-width: 600px; margin: 0 auto; }
    #search-input { width: 100%; padding: 18px 30px; border: 1px solid #dfe1e5; border-radius: 30px; font-size: 1.1em; outline: none; transition: 0.2s; }
    #search-input:focus { box-shadow: 0 1px 6px rgba(32,33,36,0.28); }

    .container { max-width: 1200px; margin: 40px auto; padding: 0 25px; }
    .section-header { margin: 60px 0 25px; display: flex; align-items: center; font-size: 1.5em; font-weight: 600; color: #5f6368; }
    .fi { margin-right: 12px; border-radius: 3px; }

    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(360px, 1fr)); gap: 24px; }
    .card { background: var(--card); border: 1px solid #dadce0; border-radius: 12px; padding: 24px; text-decoration: none; color: inherit; transition: 0.2s; display: flex; flex-direction: column; justify-content: space-between; }
    .card:hover { border-color: var(--primary); box-shadow: 0 4px 12px rgba(0,0,0,0.08); }
    
    .card-top h3 { margin: 0 0 10px; color: var(--primary); font-size: 1.2em; }
    .card-top p { font-size: 0.95em; color: #5f6368; line-height: 1.5; }
    
    .card-meta { margin-top: 20px; display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f1f3f4; padding-top: 15px; }
    .pet-icons { font-size: 1.2em; filter: grayscale(100%); opacity: 0.3; transition: 0.3s; }
    .pet-icons.active { filter: grayscale(0%); opacity: 1; }
    .read-more { font-size: 0.85em; font-weight: 600; color: var(--primary); }
</style>
</head>
<body>
<div class="hero">
    <h1>Pet Entry Guide</h1>
    <p>Find specific 2026 requirements for your pet's international journey.</p>
    <div class="search-box"><input type="text" id="search-input" placeholder="Search by destination or keyword..."></div>
</div>

<div class="container" id="main-content">
    [[CONTENT_SECTIONS]]
</div>

<script>
    const searchInput = document.getElementById('search-input');
    const cards = document.querySelectorAll('.card');
    const headers = document.querySelectorAll('.section-header');

    searchInput.addEventListener('input', (e) => {
        const term = e.target.value.toLowerCase();
        headers.forEach(header => {
            const grid = header.nextElementSibling;
            let hasVisible = false;
            grid.querySelectorAll('.card').forEach(card => {
                const match = card.innerText.toLowerCase().includes(term);
                card.style.display = match ? 'flex' : 'none';
                if (match) hasVisible = true;
            });
            header.style.display = hasVisible ? 'flex' : 'none';
            grid.style.display = hasVisible ? 'grid' : 'none';
        });
    });
</script>
</body>
</html>
"""

def main():
    # 扩展国家代码
    country_map = {
        'china': {'name': 'China', 'code': 'cn'}, 'japan': {'name': 'Japan', 'code': 'jp'},
        'korea': {'name': 'South Korea', 'code': 'kr'}, 'singapore': {'name': 'Singapore', 'code': 'sg'},
        'australia': {'name': 'Australia', 'code': 'au'}, 'canada': {'name': 'Canada', 'code': 'ca'},
        'uk': {'name': 'United Kingdom', 'code': 'gb'}, 'eu': {'name': 'Europe', 'code': 'eu'},
        'mexico': {'name': 'Mexico', 'code': 'mx'}, 'usa': {'name': 'USA/Global', 'code': 'us'}
    }

    if not os.path.exists('topics.csv'): return
    with open('topics.csv', 'r', encoding='utf-8') as f:
        rows = list(csv.reader(f))[1:]
        rows = [r for r in rows if len(r) >= 2 and r[0].strip()]

    today = datetime.now().strftime('%b %d, %Y')
    grouped = {}
    for slug, title, content in rows:
        c_key = slug.split('-')[0]
        info = country_map.get(c_key, {'name': 'Others', 'code': 'un'})
        if info['name'] not in grouped: grouped[info['name']] = {'code': info['code'], 'items': []}
        
        # 智能宠物类型检测
        has_dog = 'dog' in title.lower() or 'dog' in slug or 'both' in slug
        has_cat = 'cat' in title.lower() or 'cat' in slug or 'both' in slug
        
        grouped[info['name']]['items'].append({
            'slug': slug, 'title': title, 'content': content, 
            'has_dog': has_dog, 'has_cat': has_cat
        })

        # 生成文章页
        page_html = PAGE_TEMPLATE.replace('[[TITLE]]', title).replace('[[BODY]]', content).replace('[[TODAY]]', today)\
                     .replace('[[COUNTRY_NAME]]', info['name']).replace('[[COUNTRY_ID]]', info['name'].replace(' ', '-'))
        with open(f"{slug}.html", 'w', encoding='utf-8') as f_out: f_out.write(page_html)

    content_sections = ""
    for country in sorted(grouped.keys()):
        code = grouped[country]['code']
        country_id = country.replace(' ', '-')
        content_sections += f'<div class="section-header" id="{country_id}"><span class="fi fi-{code}"></span>{country}</div><div class="grid">'
        for item in grouped[country]['items']:
            dog_class = "active" if item['has_dog'] else ""
            cat_class = "active" if item['has_cat'] else ""
            snippet = item['content'].replace('<p>', '').replace('</p>', '').replace('<strong>', '').replace('</strong>', '')[:110] + "..."
            content_sections += f'''
            <a href="{item["slug"]}.html" class="card">
                <div class="card-top">
                    <h3>{item["title"]}</h3>
                    <p>{snippet}</p>
                </div>
                <div class="card-meta">
                    <div class="pet-icons">
                        <span class="{dog_class}">🐶</span>
                        <span class="{cat_class}">🐱</span>
                    </div>
                    <span class="read-more">View Guide →</span>
                </div>
            </a>
            '''
        content_sections += '</div>'

    index_html = INDEX_TEMPLATE.replace('[[CONTENT_SECTIONS]]', content_sections)
    with open('index.html', 'w', encoding='utf-8') as f_idx: f_idx.write(index_html)

if __name__ == "__main__":
    import csv
    main()
