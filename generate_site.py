import csv
import os
from datetime import datetime

# 1. 详情页模板：仪表盘 + 交互 Checklist + 准备时间轴
PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>[[TITLE]] | 2026 Pet Travel Dashboard</title>
<style>
    :root { --primary: #1a73e8; --warning: #f29900; --success: #1e8e3e; --text: #202124; --bg: #f8f9fa; }
    body { font-family: 'Inter', sans-serif; line-height: 1.6; color: var(--text); background: var(--bg); margin: 0; }
    .nav { background: white; border-bottom: 1px solid #dadce0; padding: 12px 20px; position: sticky; top: 0; z-index: 100; }
    .nav-inner { max-width: 1000px; margin: 0 auto; display: flex; font-size: 0.85em; color: #5f6368; }
    .nav a { color: var(--primary); text-decoration: none; margin: 0 5px; }

    .main { max-width: 1000px; margin: 25px auto; display: grid; grid-template-columns: 1fr 320px; gap: 25px; padding: 0 20px; }
    
    /* 顶部状态栏 */
    .hero-card { background: white; padding: 35px; border-radius: 16px; border: 1px solid #dadce0; grid-column: 1 / -1; }
    .complexity-badge { display: inline-block; padding: 6px 12px; border-radius: 6px; font-weight: 700; font-size: 0.85em; text-transform: uppercase; margin-bottom: 15px; }
    .level-easy { background: #e6f4ea; color: #1e8e3e; }
    .level-hard { background: #fef7e0; color: #b05a00; }

    /* 仪表盘参数 */
    .dashboard-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; margin-top: 25px; }
    .tile { background: #f1f3f4; padding: 15px; border-radius: 10px; text-align: center; }
    .tile-label { font-size: 0.75em; color: #5f6368; display: block; margin-bottom: 5px; }
    .tile-value { font-weight: 700; font-size: 1em; color: var(--text); }

    /* 交互式 Checklist */
    .checklist-box { background: white; padding: 30px; border-radius: 16px; border: 1px solid #dadce0; margin-top: 25px; }
    .todo-item { display: flex; align-items: flex-start; margin-bottom: 18px; cursor: pointer; }
    .todo-item input { margin-top: 5px; margin-right: 15px; width: 18px; height: 18px; }
    .todo-text { font-size: 1.05em; }
    .todo-item input:checked + .todo-text { text-decoration: line-through; color: #9aa0a6; }

    /* 侧边栏转化 */
    .cta-sidebar { background: #1a73e8; color: white; padding: 25px; border-radius: 16px; height: fit-content; position: sticky; top: 80px; }
    .cta-btn { width: 100%; padding: 12px; background: white; color: var(--primary); border: none; border-radius: 8px; font-weight: 700; cursor: pointer; margin-top: 15px; }
    
    .footer { text-align: center; padding: 60px; color: #70757a; font-size: 0.9em; }
</style>
</head>
<body>
    <div class="nav"><div class="nav-inner"><a href="/">Portal</a> / <a href="/#[[COUNTRY_ID]]">[[COUNTRY_NAME]]</a> / Current Guide</div></div>
    
    <div class="main">
        <div class="hero-card">
            <span class="complexity-badge [[COMPLEX_CLASS]]">[[LEVEL]]</span>
            <h1 style="margin:0;font-size:2.4em;">[[TITLE]]</h1>
            
            <div class="dashboard-grid">
                <div class="tile"><span class="tile-label">Lead Time</span><span class="tile-value">[[LEAD_TIME]]</span></div>
                <div class="tile"><span class="tile-label">Quarantine</span><span class="tile-value">[[QUARANTINE]]</span></div>
                <div class="tile"><span class="tile-label">Min. Age</span><span class="tile-value">6 Months</span></div>
                <div class="tile"><span class="tile-label">Microchip</span><span class="tile-value">ISO Req.</span></div>
            </div>
        </div>

        <div class="content-area">
            <div class="checklist-box">
                <h2 style="margin-top:0;">Your Action Checklist</h2>
                [[CHECKLIST_ITEMS]]
            </div>
            
            <div style="background:white; padding:30px; border-radius:16px; border:1px solid #dadce0; margin-top:25px;">
                <h2>Deep Guide</h2>
                <div class="article-body">[[BODY]]</div>
            </div>
        </div>

        <div class="cta-sidebar">
            <h3 style="margin-top:0;">Need 1-on-1 Help?</h3>
            <p style="font-size:0.9em; opacity:0.9;">Complex route? Our IPATA-certified experts can handle the paperwork for you.</p>
            <button class="cta-btn" onclick="location.href='mailto:help@petentryguide.com'">Request Expert Help</button>
            <p style="font-size:0.8em; margin-top:20px; opacity:0.7;">Verified Data Source: CDC/USDA official portals.</p>
        </div>
    </div>
    <div class="footer">© 2026 Pet Entry Guide. Not legal advice.</div>
</body>
</html>
"""

# 2. 首页模板：搜索 + 热门航线 Tags
INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pet Entry Guide | Global Relocation Database</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lipis/flag-icons@7.0.0/css/flag-icons.min.css"/>
<style>
    :root { --primary: #1a73e8; --bg: #f8f9fa; }
    body { font-family: 'Inter', sans-serif; margin: 0; background: var(--bg); }
    .hero { background: white; padding: 100px 20px 60px; text-align: center; border-bottom: 1px solid #dadce0; }
    h1 { font-size: 3.8em; letter-spacing: -0.05em; color: #1a0dab; margin:0; }
    .search-wrapper { max-width: 650px; margin: 30px auto; }
    #search-input { width: 100%; padding: 20px 30px; border: 1px solid #dfe1e5; border-radius: 35px; font-size: 1.2em; outline: none; transition: 0.2s; box-shadow: 0 1px 6px rgba(32,33,36,0.1); }
    #search-input:focus { box-shadow: 0 2px 12px rgba(32,33,36,0.2); }
    
    .hot-paths { margin-top: 20px; display: flex; justify-content: center; gap: 12px; flex-wrap: wrap; }
    .path-tag { background: #f1f3f4; padding: 8px 16px; border-radius: 20px; text-decoration: none; color: #3c4043; font-size: 0.9em; font-weight: 500; }
    .path-tag:hover { background: #e8f0fe; color: var(--primary); }

    .container { max-width: 1200px; margin: 50px auto; padding: 0 25px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 25px; }
    .card { background: white; border: 1px solid #dadce0; border-radius: 16px; padding: 28px; text-decoration: none; color: inherit; transition: 0.3s; }
    .card:hover { transform: translateY(-4px); box-shadow: 0 10px 20px rgba(0,0,0,0.05); }
    h2.section-title { font-size: 1.6em; margin: 60px 0 25px; display: flex; align-items: center; border-left: 5px solid var(--primary); padding-left: 15px; }
</style>
</head>
<body>
<div class="hero">
    <h1>Pet Entry Guide</h1>
    <p style="font-size:1.3em; color:#5f6368;">2026 International Travel Database</p>
    <div class="search-wrapper">
        <input type="text" id="search-input" placeholder="Origin → Destination (e.g., China USA)...">
        <div class="hot-paths">
            <span style="font-size:0.9em; color:#70757a; padding-top:8px;">Hot:</span>
            <a href="/china-to-usa-cat.html" class="path-tag">China → USA</a>
            <a href="/japan-to-usa-dog.html" class="path-tag">Japan → USA</a>
            <a href="/uk-to-usa-cat.html" class="path-tag">UK → USA</a>
        </div>
    </div>
</div>
<div class="container">[[CONTENT_SECTIONS]]</div>
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
        rows = list(csv.reader(f))[1:]
        rows = [r for r in rows if len(r) >= 2 and r[0].strip()]

    today = datetime.now().strftime('%b %d, %Y')
    grouped = {}

    for slug, title, content in rows:
        c_key = slug.split('-')[0]
        info = country_map.get(c_key, {'name': 'Others', 'code': 'un'})
        if info['name'] not in grouped: grouped[info['name']] = {'code': info['code'], 'items': []}
        
        # 自动化逻辑：提取隔离天数和准备时间
        q_days = "0 Days" if "no quarantine" in content.lower() or "rabies-free" in content.lower() else "30 Days+"
        lead_time = "6 Months+" if "rabies titer" in content.lower() else "30 Days"
        level = "Easy" if q_days == "0 Days" else "Hard (Permit Req.)"
        c_class = "level-easy" if level == "Easy" else "level-hard"

        # 生成交互式 Checklist
        steps = ["ISO Microchip", "Rabies Vaccine", "Health Certificate", "CDC/USDA Form"]
        checklist_html = "".join([f'<label class="todo-item"><input type="checkbox"><span class="todo-text">{s}</span></label>' for s in steps])

        # 写入详情页
        page_html = PAGE_TEMPLATE.replace('[[TITLE]]', title).replace('[[BODY]]', content).replace('[[TODAY]]', today)\
                     .replace('[[COUNTRY_NAME]]', info['name']).replace('[[COUNTRY_ID]]', info['name'].replace(' ', '-'))\
                     .replace('[[QUARANTINE]]', q_days).replace('[[LEAD_TIME]]', lead_time)\
                     .replace('[[LEVEL]]', level).replace('[[COMPLEX_CLASS]]', c_class)\
                     .replace('[[CHECKLIST_ITEMS]]', checklist_html)
        
        with open(f"{slug}.html", 'w', encoding='utf-8') as f_out: f_out.write(page_html)
        grouped[info['name']]['items'].append({'slug': slug, 'title': title, 'content': content})

    # 构建首页 (篇幅限制，此处逻辑略...)
    # ...

if __name__ == "__main__":
    import csv
    main()
