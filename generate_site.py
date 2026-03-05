import csv
import os
from datetime import datetime

# 1. 文章详情页模板 (PM 4.0：仪表盘 + 交互式 Checklist)
PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>[[TITLE]] | 2026 Pet Travel Dashboard</title>
<style>
    :root { --primary: #1a73e8; --text: #202124; --bg: #ffffff; --accent: #f8f9fa; }
    body { font-family: 'Inter', -apple-system, sans-serif; line-height: 1.7; color: var(--text); background: var(--bg); margin: 0; padding: 0; }
    .nav { border-bottom: 1px solid #eee; padding: 15px 20px; background: white; position: sticky; top: 0; z-index: 100; }
    .nav-inner { max-width: 900px; margin: 0 auto; display: flex; justify-content: space-between; font-size: 0.9em; }
    .container { max-width: 900px; margin: 40px auto; padding: 0 20px; display: grid; grid-template-columns: 1fr 300px; gap: 30px; }
    
    .main-content { background: white; padding: 40px; border-radius: 16px; border: 1px solid #dadce0; }
    .sidebar { background: #e8f0fe; padding: 25px; border-radius: 16px; height: fit-content; position: sticky; top: 80px; }
    
    h1 { font-size: 2.4em; letter-spacing: -0.02em; line-height: 1.2; margin-bottom: 20px; }
    .status-badge { background: #e6f4ea; color: #1e8e3e; padding: 6px 12px; border-radius: 6px; font-weight: 600; font-size: 0.85em; display: inline-block; margin-bottom: 15px; }
    
    .checklist { margin-top: 30px; padding: 20px; background: #fff; border: 1px solid #eee; border-radius: 12px; }
    .todo { display: flex; align-items: center; margin-bottom: 12px; cursor: pointer; }
    .todo input { margin-right: 12px; width: 18px; height: 18px; }
    
    .footer { margin-top: 80px; padding: 40px; text-align: center; border-top: 1px solid #eee; color: #70757a; font-size: 0.9em; }
    @media (max-width: 800px) { .container { grid-template-columns: 1fr; } }
</style>
</head>
<body>
    <div class="nav"><div class="nav-inner"><a href="/" style="color:var(--primary);text-decoration:none;font-weight:600;">Pet Entry Guide</a><span>2026 Guide</span></div></div>
    <div class="container">
        <div class="main-content">
            <div class="status-badge">● Verified for 2026</div>
            <h1>[[TITLE]]</h1>
            <div class="content">[[BODY]]</div>
            <div class="checklist">
                <h3>Action Checklist</h3>
                <label class="todo"><input type="checkbox"> 15-digit ISO Microchip</label>
                <label class="todo"><input type="checkbox"> Valid Rabies Certificate</label>
                <label class="todo"><input type="checkbox"> Endorsed Export Health Certificate</label>
                <label class="todo"><input type="checkbox"> CDC Import Form (if required)</label>
            </div>
        </div>
        <div class="sidebar">
            <h3 style="margin-top:0;">Route Info</h3>
            <p><strong>Lead Time:</strong> 30 - 180 Days</p>
            <p><strong>Quarantine:</strong> [[QUARANTINE]]</p>
            <button onclick="window.print()" style="width:100%;padding:12px;background:var(--primary);color:white;border:none;border-radius:8px;font-weight:600;cursor:pointer;">Save as PDF</button>
        </div>
    </div>
</body>
</html>
"""

# 2. 首页门户模板 (PM 4.0：极简搜索 + 热门路径)
INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pet Entry Guide | 2026 USA Pet Travel Portal</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lipis/flag-icons@7.0.0/css/flag-icons.min.css"/>
<style>
    :root { --primary: #1a73e8; --text: #202124; --bg: #f8f9fa; }
    body { font-family: 'Inter', sans-serif; color: var(--text); background: var(--bg); margin: 0; }
    .hero { background: white; padding: 100px 20px 60px; text-align: center; border-bottom: 1px solid #eee; }
    h1 { font-size: 3.8em; letter-spacing: -0.05em; color: #1a0dab; margin-bottom: 20px; }
    
    .search-container { max-width: 650px; margin: 0 auto; position: relative; }
    #search-input { width: 100%; padding: 20px 30px; border: 1px solid #dfe1e5; border-radius: 35px; font-size: 1.2em; outline: none; transition: 0.2s; box-shadow: 0 1px 6px rgba(32,33,36,0.1); }
    #search-input:focus { box-shadow: 0 2px 12px rgba(32,33,36,0.2); }

    /* 热门路径标签 */
    .hot-paths { margin-top: 25px; display: flex; justify-content: center; gap: 10px; flex-wrap: wrap; }
    .path-tag { background: #f1f3f4; padding: 8px 18px; border-radius: 20px; text-decoration: none; color: #3c4043; font-size: 0.9em; font-weight: 500; transition: 0.2s; }
    .path-tag:hover { background: #e8f0fe; color: var(--primary); }

    .container { max-width: 1200px; margin: 50px auto; padding: 0 25px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 24px; }
    .card { background: white; border: 1px solid #dadce0; border-radius: 12px; padding: 24px; text-decoration: none; color: inherit; transition: 0.2s; display: flex; flex-direction: column; }
    .card:hover { transform: translateY(-3px); box-shadow: 0 8px 16px rgba(0,0,0,0.06); border-color: var(--primary); }
    .section-title { font-size: 1.5em; margin: 60px 0 20px; display: flex; align-items: center; color: #5f6368; }
</style>
</head>
<body>
<div class="hero">
    <h1>Pet Entry Guide</h1>
    <div class="search-container">
        <input type="text" id="search-input" placeholder="Origin → USA (e.g. China, UK)...">
    </div>
    <div class="hot-paths">
        <span style="color:#70757a; font-size:0.9em; padding-top:8px;">Popular:</span>
        <a href="/china-to-usa-dog.html" class="path-tag">China → USA</a>
        <a href="/australia-to-usa-dog.html" class="path-tag">Australia → USA</a>
        <a href="/japan-to-usa-cat.html" class="path-tag">Japan → USA</a>
    </div>
</div>
<div class="container">[[CONTENT_SECTIONS]]</div>

<script>
    const searchInput = document.getElementById('search-input');
    const cards = document.querySelectorAll('.card');
    searchInput.addEventListener('input', (e) => {
        const term = e.target.value.toLowerCase();
        cards.forEach(card => {
            const isMatch = card.innerText.toLowerCase().includes(term);
            card.style.display = isMatch ? 'flex' : 'none';
        });
    });
</script>
</body>
</html>
"""

def main():
    country_map = {
        'china': {'name': 'China', 'code': 'cn'}, 'japan': {'name': 'Japan', 'code': 'jp'},
        'australia': {'name': 'Australia', 'code': 'au'}, 'uk': {'name': 'United Kingdom', 'code': 'gb'},
        'usa': {'name': 'General/USA', 'code': 'us'}
    }

    if not os.path.exists('topics.csv'): return
    with open('topics.csv', 'r', encoding='utf-8') as f:
        rows = [r for r in list(csv.reader(f))[1:] if len(r) >= 2 and r[0].strip()]

    today = datetime.now().strftime('%b %Y')
    grouped = {}
    for slug, title, content in rows:
        c_key = slug.split('-')[0]
        info = country_map.get(c_key, {'name': 'Other', 'code': 'un'})
        if info['name'] not in grouped: grouped[info['name']] = {'code': info['code'], 'items': []}
        
        q_days = "None" if "no quarantine" in content.lower() or "rabies-free" in content.lower() else "30 Days+"
        
        # 写入文章页
        html = PAGE_TEMPLATE.replace('[[TITLE]]', title).replace('[[BODY]]', content).replace('[[TODAY]]', today)\
                     .replace('[[COUNTRY_NAME]]', info['name']).replace('[[COUNTRY_ID]]', info['name'].replace(' ', '-'))\
                     .replace('[[QUARANTINE]]', q_days)
        with open(f"{slug}.html", 'w', encoding='utf-8') as f_out: f_out.write(html)
        grouped[info['name']]['items'].append({'slug': slug, 'title': title, 'content': content})

    sections = ""
    for country in sorted(grouped.keys()):
        code = grouped[country]['code']
        sections += f'<h2 class="section-title"><span class="fi fi-{code}"></span>&nbsp;{country}</h2><div class="grid">'
        for item in grouped[country]['items']:
            snippet = item['content'].replace('<p>', '').replace('</p>', '')[:100] + "..."
            sections += f'<a href="{item["slug"]}.html" class="card"><h3>{item["title"]}</h3><p>{snippet}</p></a>'
        sections += '</div>'

    with open('index.html', 'w', encoding='utf-8') as f_idx:
        f_idx.write(INDEX_TEMPLATE.replace('[[CONTENT_SECTIONS]]', sections))

if __name__ == "__main__":
    import csv
    main()
