import csv
import os
from datetime import datetime

# 1. 文章详情页模板 (增加了“检查清单”侧边栏感)
PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>[[TITLE]] | 2026 Pet Entry Guide</title>
<style>
    :root { --primary: #1a73e8; --text: #202124; --bg: #ffffff; --accent: #e8f0fe; }
    body { font-family: 'Inter', -apple-system, sans-serif; line-height: 1.7; color: var(--text); background: var(--bg); margin: 0; padding: 0; }
    .nav-bar { border-bottom: 1px solid #eee; padding: 15px 20px; background: white; position: sticky; top: 0; z-index: 100; }
    .nav-content { max-width: 800px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; }
    .container { max-width: 800px; margin: 40px auto; padding: 0 20px; }
    h1 { font-size: 2.6em; color: var(--text); line-height: 1.2; letter-spacing: -0.02em; margin-bottom: 10px; }
    .meta { font-size: 0.95em; color: #70757a; margin-bottom: 40px; }
    .content { font-size: 1.15em; }
    .content p { margin-bottom: 24px; }
    .content strong { color: var(--primary); background: var(--accent); padding: 2px 6px; border-radius: 4px; }
    .checklist { background: #fdf6e3; border: 1px solid #eddeaf; padding: 25px; border-radius: 12px; margin: 40px 0; }
    .checklist h3 { margin-top: 0; color: #856404; }
    .footer { margin-top: 80px; padding: 40px; text-align: center; border-top: 1px solid #eee; color: #70757a; font-size: 0.9em; }
    a { color: var(--primary); text-decoration: none; font-weight: 500; }
</style>
</head>
<body>
    <div class="nav-bar"><div class="nav-content"><a href="/">← Pet Entry Guide</a><span>2026 Updated</span></div></div>
    <div class="container">
        <h1>[[TITLE]]</h1>
        <p class="meta">Verified Guide • Updated [[TODAY]]</p>
        <div class="content">[[BODY]]</div>
        <div class="checklist">
            <h3>Quick Checklist</h3>
            <p>1. ISO Microchip (15-digit)<br>2. Rabies Vaccination Certificate<br>3. CDC Dog Import Form (if applicable)<br>4. Airline Reservation</p>
        </div>
    </div>
    <div class="footer">© 2026 Pet Entry Guide. Not legal advice.</div>
</body>
</html>
"""

# 2. 首页门户模板 (PM 风格：简洁、带分类)
INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pet Entry Guide | 2026 USA Pet Travel Portal</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lipis/flag-icons@7.0.0/css/flag-icons.min.css"/>
<style>
    :root { --primary: #1a73e8; --text: #202124; --bg: #f8f9fa; }
    body { font-family: 'Inter', sans-serif; color: var(--text); background: var(--bg); margin: 0; }
    .hero { background: white; padding: 80px 20px 40px; text-align: center; border-bottom: 1px solid #eee; }
    h1 { font-size: 3.5em; letter-spacing: -0.05em; margin-bottom: 20px; color: #1a0dab; }
    
    .search-container { max-width: 600px; margin: 0 auto; position: relative; }
    #search-input { width: 100%; padding: 18px 30px; border: 1px solid #dfe1e5; border-radius: 30px; font-size: 1.1em; transition: 0.2s; box-shadow: none; outline: none; box-sizing: border-box; }
    #search-input:hover, #search-input:focus { box-shadow: 0 1px 6px rgba(32,33,36,0.28); border-color: transparent; }

    .filter-bar { display: flex; justify-content: center; gap: 15px; margin-top: 25px; }
    .filter-btn { padding: 8px 20px; border-radius: 20px; border: 1px solid #dadce0; background: white; cursor: pointer; font-size: 0.9em; transition: 0.2s; }
    .filter-btn.active { background: var(--primary); color: white; border-color: var(--primary); }

    .container { max-width: 1100px; margin: 40px auto; padding: 0 20px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 24px; }
    
    .card { background: white; border: 1px solid #dadce0; border-radius: 12px; padding: 24px; text-decoration: none; color: inherit; display: flex; flex-direction: column; transition: 0.2s; }
    .card:hover { box-shadow: 0 4px 12px rgba(0,0,0,0.1); transform: translateY(-2px); }
    
    /* 语义化标签样式 */
    .badge-row { display: flex; gap: 8px; margin-bottom: 12px; }
    .badge { font-size: 0.75em; font-weight: 700; padding: 2px 8px; border-radius: 4px; text-transform: uppercase; }
    .badge-dog { background: #e8f0fe; color: #1967d2; }
    .badge-cat { background: #fef7e0; color: #ea8600; }
    
    h3 { margin: 0 0 10px; font-size: 1.2em; line-height: 1.4; color: var(--primary); }
    p { margin: 0; font-size: 0.9em; color: #5f6368; overflow: hidden; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; }
    
    .section-title { font-size: 1.4em; margin: 60px 0 20px; display: flex; align-items: center; color: #70757a; }
    .fi { margin-right: 10px; border-radius: 2px; }
</style>
</head>
<body>
<div class="hero">
    <h1>Pet Entry Guide</h1>
    <div class="search-container">
        <input type="text" id="search-input" placeholder="Search by country or keywords...">
    </div>
    <div class="filter-bar">
        <button class="filter-btn active" onclick="filterType('all', this)">All</button>
        <button class="filter-btn" onclick="filterType('dog', this)">Dogs Only</button>
        <button class="filter-btn" onclick="filterType('cat', this)">Cats Only</button>
    </div>
</div>

<div class="container">
    [[CONTENT_SECTIONS]]
</div>

<script>
    const searchInput = document.getElementById('search-input');
    const cards = document.querySelectorAll('.card');

    function filterType(type, btn) {
        // 更新按钮状态
        document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        
        // 执行过滤
        cards.forEach(card => {
            const isMatch = type === 'all' || card.getAttribute('data-type') === type || card.getAttribute('data-type') === 'both';
            card.style.display = isMatch ? 'flex' : 'none';
        });
        // 隐藏空标题
        document.querySelectorAll('.section-title').forEach(title => {
            const grid = title.nextElementSibling;
            const hasVisible = Array.from(grid.querySelectorAll('.card')).some(c => c.style.display !== 'none');
            title.style.display = hasVisible ? 'flex' : 'none';
            grid.style.display = hasVisible ? 'grid' : 'none';
        });
    }

    searchInput.addEventListener('input', (e) => {
        const term = e.target.value.toLowerCase();
        cards.forEach(card => {
            const text = card.innerText.toLowerCase();
            card.style.display = text.includes(term) ? 'flex' : 'none';
        });
        // 逻辑同上
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
        'mexico': {'name': 'Mexico', 'code': 'mx'}, 'usa': {'name': 'General/USA', 'code': 'us'}
    }

    if not os.path.exists('topics.csv'): return
    with open('topics.csv', 'r', encoding='utf-8') as f:
        rows = list(csv.reader(f))[1:]
        rows = [r for r in rows if len(r) >= 2 and r[0].strip()]

    today = datetime.now().strftime('%b %Y')
    grouped = {}
    for slug, title, content in rows:
        c_key = slug.split('-')[0]
        info = country_map.get(c_key, {'name': 'Other', 'code': 'us'})
        if info['name'] not in grouped: grouped[info['name']] = {'code': info['code'], 'items': []}
        
        # 语义识别逻辑：识别 Dog/Cat
        p_type = 'both'
        if 'dog' in title.lower() or 'dog' in slug: p_type = 'dog'
        elif 'cat' in title.lower() or 'cat' in slug: p_type = 'cat'
        
        grouped[info['name']]['items'].append({'slug': slug, 'title': title, 'content': content, 'type': p_type})

        # 生成文章页
        html = PAGE_TEMPLATE.replace('[[TITLE]]', title).replace('[[TODAY]]', today).replace('[[BODY]]', content)
        with open(f"{slug}.html", 'w', encoding='utf-8') as f_out: f_out.write(html)

    content_sections = ""
    for country in sorted(grouped.keys()):
        code = grouped[country]['code']
        content_sections += f'<h2 class="section-title"><span class="fi fi-{code}"></span>{country}</h2><div class="grid">'
        for item in grouped[country]['items']:
            badge = f'<span class="badge badge-{item["type"]}">{item["type"]}</span>' if item['type'] != 'both' else '<span class="badge badge-dog">Dog</span><span class="badge badge-cat">Cat</span>'
            snippet = item['content'].replace('<p>', '').replace('</p>', '')[:100] + "..."
            content_sections += f'''
            <a href="{item["slug"]}.html" class="card" data-type="{item["type"]}">
                <div class="badge-row">{badge}</div>
                <h3>{item["title"]}</h3>
                <p>{snippet}</p>
            </a>
            '''
        content_sections += '</div>'

    index_html = INDEX_TEMPLATE.replace('[[CONTENT_SECTIONS]]', content_sections)
    with open('index.html', 'w', encoding='utf-8') as f_idx: f_idx.write(index_html)

if __name__ == "__main__":
    import csv
    main()
