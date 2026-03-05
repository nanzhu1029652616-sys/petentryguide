import csv
import os
from datetime import datetime

# 1. 详情页模板 (PM 5.0 仪表盘风 + 交互式 Checklist)
PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>[[TITLE]] | 2026 Pet Travel Dashboard</title>
<style>
    :root { --primary: #1a73e8; --warning: #f29900; --success: #1e8e3e; --text: #202124; --bg: #f8f9fa; }
    body { font-family: 'Inter', -apple-system, sans-serif; line-height: 1.6; color: var(--text); background: var(--bg); margin: 0; }
    .nav { background: white; border-bottom: 1px solid #dadce0; padding: 12px 20px; position: sticky; top: 0; z-index: 100; }
    .nav-inner { max-width: 1100px; margin: 0 auto; display: flex; font-size: 0.85em; color: #5f6368; }
    .nav a { color: var(--primary); text-decoration: none; margin: 0 5px; }
    .main { max-width: 1100px; margin: 30px auto; display: grid; grid-template-columns: 1fr 320px; gap: 30px; padding: 0 20px; }
    .dashboard-header { background: white; padding: 40px; border-radius: 20px; border: 1px solid #dadce0; grid-column: 1 / -1; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
    .complexity-badge { display: inline-block; padding: 6px 14px; border-radius: 8px; font-weight: 800; font-size: 0.8em; text-transform: uppercase; margin-bottom: 15px; }
    .level-easy { background: #e6f4ea; color: #1e8e3e; }
    .level-hard { background: #fff4e5; color: #b05a00; border: 1px solid #ffe2b5; }
    .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 20px; margin-top: 30px; }
    .stat-tile { background: #f8f9fa; padding: 20px; border-radius: 12px; text-align: center; border: 1px solid #eee; }
    .stat-label { font-size: 0.75em; color: #70757a; text-transform: uppercase; letter-spacing: 0.05em; display: block; margin-bottom: 8px; }
    .stat-value { font-weight: 700; font-size: 1.1em; color: #1a1c1e; }
    .content-box { background: white; padding: 40px; border-radius: 20px; border: 1px solid #dadce0; margin-top: 30px; }
    .todo-item { display: flex; align-items: flex-start; padding: 15px; border-bottom: 1px solid #f1f3f4; cursor: pointer; }
    .todo-item input { margin-top: 4px; margin-right: 15px; width: 20px; height: 20px; }
    .todo-item input:checked + span { text-decoration: line-through; color: #9aa0a6; }
    .sidebar-cta { background: #1a73e8; color: white; padding: 30px; border-radius: 20px; position: sticky; top: 100px; text-align: center; }
    .cta-button { width: 100%; padding: 15px; background: white; color: #1a73e8; border: none; border-radius: 10px; font-weight: 700; margin-top: 20px; cursor: pointer; }
    .footer { text-align: center; padding: 80px 20px; color: #70757a; font-size: 0.9em; }
    @media (max-width: 800px) { .main { grid-template-columns: 1fr; } }
</style>
</head>
<body>
    <div class="nav"><div class="nav-inner"><a href="/">Home</a> / <a href="/#[[COUNTRY_ID]]">[[COUNTRY_NAME]]</a> / [[TITLE]]</div></div>
    <div class="main">
        <header class="dashboard-header">
            <span class="complexity-badge [[COMPLEX_CLASS]]">[[LEVEL]]</span>
            <h1 style="margin:0; font-size:2.8em;">[[TITLE]]</h1>
            <div class="stats-grid">
                <div class="stat-tile"><span class="stat-label">Lead Time</span><span class="stat-value">[[LEAD_TIME]]</span></div>
                <div class="stat-tile"><span class="stat-label">Quarantine</span><span class="stat-value">[[QUARANTINE]]</span></div>
                <div class="stat-tile"><span class="stat-label">Pet Type</span><span class="stat-value">[[PET_TYPE]]</span></div>
                <div class="stat-tile"><span class="stat-label">Source</span><span class="stat-value">CDC 2026</span></div>
            </div>
        </header>
        <section class="content-area">
            <div class="content-box">
                <h2 style="margin:0 0 20px;">Relocation Checklist</h2>
                [[CHECKLIST_ITEMS]]
            </div>
            <div class="content-box">
                <h2 style="margin-top:0;">Deep Guide</h2>
                <div style="font-size:1.1em; line-height:1.8;">[[BODY]]</div>
            </div>
        </section>
        <aside class="sidebar-cta">
            <h3 style="margin:0;">Expert Paperwork Support</h3>
            <p style="font-size:0.9em; opacity:0.9; margin-top:10px;">CDC import forms can be tricky. Let our partners handle the 2026 requirements for you.</p>
            <button class="cta-button" onclick="window.print()">Download Checklist PDF</button>
        </aside>
    </div>
    <footer class="footer">© 2026 Pet Entry Guide. Verified against latest CDC protocols.</footer>
</body>
</html>
"""

# 2. 首页模板 (带搜索与热门路径)
INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pet Entry Guide | 2026 Global Pet Relocation Database</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lipis/flag-icons@7.0.0/css/flag-icons.min.css"/>
<style>
    :root { --primary: #1a73e8; --bg: #f8f9fa; }
    body { font-family: 'Inter', sans-serif; margin: 0; background: var(--bg); color: #202124; }
    .hero { background: white; padding: 100px 20px 80px; text-align: center; border-bottom: 1px solid #dadce0; }
    h1 { font-size: 4em; letter-spacing: -0.05em; color: #1a0dab; margin:0; line-height:1; }
    .search-ui { max-width: 650px; margin: 40px auto 0; }
    #search-input { width: 100%; padding: 22px 35px; border: 1px solid #dfe1e5; border-radius: 40px; font-size: 1.25em; outline: none; box-shadow: 0 2px 8px rgba(0,0,0,0.05); transition: 0.3s; }
    .hot-routes { margin-top: 25px; display: flex; justify-content: center; gap: 12px; flex-wrap: wrap; }
    .route-tag { background: #f1f3f4; padding: 10px 20px; border-radius: 25px; text-decoration: none; color: #3c4043; font-size: 0.95em; font-weight: 600; }
    .route-tag:hover { background: #e8f0fe; color: var(--primary); }
    .container { max-width: 1200px; margin: 60px auto; padding: 0 25px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(360px, 1fr)); gap: 30px; }
    .card { background: white; border: 1px solid #dadce0; border-radius: 20px; padding: 30px; text-decoration: none; color: inherit; transition: 0.3s; display: flex; flex-direction: column; justify-content: space-between; }
    .card:hover { transform: translateY(-5px); box-shadow: 0 12px 30px rgba(0,0,0,0.08); border-color: var(--primary); }
    .section-title { font-size: 1.8em; margin: 80px 0 30px; display: flex; align-items: center; border-left: 6px solid var(--primary); padding-left: 20px; color: #5f6368; }
    .fi { margin-right: 15px; border-radius: 4px; }
</style>
</head>
<body>
<div class="hero">
    <h1>Pet Entry Guide</h1>
    <div class="search-ui">
        <input type="text" id="search-input" placeholder="Origin country (e.g. China, UK)...">
        <div class="hot-routes">
            <span style="color:#70757a; font-weight:600; padding-top:10px;">Popular:</span>
            <a href="/china-to-usa-dog.html" class="route-tag">China → USA</a>
            <a href="/australia-to-usa-dog.html" class="route-tag">Australia → USA</a>
            <a href="/south-korea-to-usa-dog.html" class="route-tag">Korea → USA</a>
        </div>
    </div>
</div>
<div class="container" id="main-content">[[CONTENT_SECTIONS]]</div>
<script>
    const searchInput = document.getElementById('search-input');
    const cards = document.querySelectorAll('.card');
    const titles = document.querySelectorAll('.section-title');
    searchInput.addEventListener('input', (e) => {
        const term = e.target.value.toLowerCase();
        titles.forEach(title => {
            const grid = title.nextElementSibling;
            let found = false;
            grid.querySelectorAll('.card').forEach(card => {
                const match = card.innerText.toLowerCase().includes(term);
                card.style.display = match ? 'flex' : 'none';
                if (match) found = true;
            });
            title.style.display = found ? 'flex' : 'none';
            grid.style.display = found ? 'grid' : 'none';
        });
    });
</script>
</body>
</html>
"""

def main():
    # 扩展映射表，解决 "Others" 过多的问题
    country_map = {
        'china': {'name': 'China', 'code': 'cn'},
        'japan': {'name': 'Japan', 'code': 'jp'},
        'south-korea': {'name': 'South Korea', 'code': 'kr'},
        'korea': {'name': 'South Korea', 'code': 'kr'},
        'singapore': {'name': 'Singapore', 'code': 'sg'},
        'australia': {'name': 'Australia', 'code': 'au'},
        'canada': {'name': 'Canada', 'code': 'ca'},
        'uk': {'name': 'United Kingdom', 'code': 'gb'},
        'usa': {'name': 'General/USA', 'code': 'us'}
    }

    if not os.path.exists('topics.csv'): return
    with open('topics.csv', 'r', encoding='utf-8') as f:
        rows = [r for r in list(csv.reader(f))[1:] if len(r) >= 2 and r[0].strip()]

    today = datetime.now().strftime('%b %d, %Y')
    grouped = {}

    for slug, title, content in rows:
        # 逻辑：识别通用指南还是国家指南
        first_part = slug.split('-')[0]
        
        if 'cost' in slug or 'general' in slug:
            c_name, c_code = 'General Guides', 'un'
        else:
            info = country_map.get(first_part, {'name': 'Other Routes', 'code': 'un'})
            c_name, c_code = info['name'], info['code']

        if c_name not in grouped: grouped[c_name] = {'code': c_code, 'items': []}
        
        # 提取仪表盘参数
        q_days = "0 Days" if "no quarantine" in content.lower() or "rabies-free" in content.lower() else "30-Day Min."
        lead_time = "6+ Months" if "rabies titer" in content.lower() else "30 Days"
        level = "High Difficulty" if q_days != "0 Days" else "Low Difficulty"
        c_class = "level-hard" if level != "Low Difficulty" else "level-easy"
        pet_type = "Dog 🐶" if "dog" in slug else "Cat 🐱"

        # 生成交互式 Checklist
        steps = ["ISO Microchip", "Rabies Vaccine", "Government Endorsement", "CDC Dog Import Form"]
        checklist_html = "".join([f'<label class="todo-item"><input type="checkbox"><span>{s}</span></label>' for s in steps])

        # 写入详情页
        page_html = PAGE_TEMPLATE.replace('[[TITLE]]', title).replace('[[BODY]]', content).replace('[[TODAY]]', today)\
                     .replace('[[COUNTRY_NAME]]', c_name).replace('[[COUNTRY_ID]]', c_name.replace(' ', '-'))\
                     .replace('[[QUARANTINE]]', q_days).replace('[[LEAD_TIME]]', lead_time)\
                     .replace('[[LEVEL]]', level).replace('[[COMPLEX_CLASS]]', c_class)\
                     .replace('[[PET_TYPE]]', pet_type).replace('[[CHECKLIST_ITEMS]]', checklist_html)
        
        with open(f"{slug}.html", 'w', encoding='utf-8') as f_out: f_out.write(page_html)
        grouped[c_name]['items'].append({'slug': slug, 'title': title, 'content': content, 'pet_type': pet_type})

    # 构建首页
    sections = ""
    sorted_countries = sorted(grouped.keys())
    if 'General Guides' in sorted_countries:
        sorted_countries.remove('General Guides'); sorted_countries.insert(0, 'General Guides')

    for country in sorted_countries:
        code = grouped[country]['code']
        sections += f'<h2 class="section-title" id="{country.replace(" ", "-")}"><span class="fi fi-{code}"></span>&nbsp;{country}</h2><div class="grid">'
        for item in grouped[country]['items']:
            snippet = item['content'].replace('<p>', '').replace('</p>', '')[:110] + "..."
            sections += f'''
            <a href="{item["slug"]}.html" class="card">
                <div>
                    <span style="font-size:0.8em; color:#70757a;">2026 GUIDE • {item["pet_type"]}</span>
                    <h3 style="color:#1a73e8; margin:10px 0;">{item["title"]}</h3>
                    <p>{snippet}</p>
                </div>
                <div style="margin-top:20px; font-weight:700; color:#1a73e8; font-size:0.9em;">Analyze Route →</div>
            </a>
            '''
        sections += '</div>'

    with open('index.html', 'w', encoding='utf-8') as f_idx:
        f_idx.write(INDEX_TEMPLATE.replace('[[CONTENT_SECTIONS]]', sections))

if __name__ == "__main__":
    main()
