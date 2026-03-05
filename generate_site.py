import csv
import os
from datetime import datetime

# 1. 详情页模板：强化“政策解读”定位
PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>[[TITLE]] | 2026 Pet Travel Dashboard</title>
<style>
    :root { --primary: #1a73e8; --text: #202124; --bg: #ffffff; --sidebar: #f8f9fa; }
    body { font-family: 'Inter', -apple-system, sans-serif; line-height: 1.6; color: var(--text); background: var(--bg); margin: 0; }
    .nav { background: white; border-bottom: 1px solid #dadce0; padding: 15px 20px; position: sticky; top: 0; z-index: 100; }
    .nav-inner { max-width: 1100px; margin: 0 auto; display: flex; font-size: 0.9em; }
    .container { max-width: 1100px; margin: 30px auto; display: grid; grid-template-columns: 1fr 320px; gap: 30px; padding: 0 20px; }
    .content-area { background: white; padding: 40px; border-radius: 20px; border: 1px solid #dadce0; }
    .policy-insight { background: #fff4e5; border: 1px solid #ffe2b5; padding: 20px; border-radius: 12px; margin-bottom: 30px; }
    h1 { font-size: 2.6em; margin: 0 0 20px; letter-spacing: -0.02em; }
    .footer { text-align: center; padding: 60px; color: #70757a; font-size: 0.9em; }
    @media (max-width: 800px) { .container { grid-template-columns: 1fr; } }
</style>
</head>
<body>
    <div class="nav"><div class="nav-inner"><a href="/" style="color:var(--primary);text-decoration:none;font-weight:600;">Pet Entry Portal</a> / [[TITLE]]</div></div>
    <div class="container">
        <div class="content-area">
            <div class="policy-insight"><strong>2026 Policy Insight:</strong> This route is verified against current CDC/USDA relocation protocols.</div>
            <h1>[[TITLE]]</h1>
            <div class="article-body">[[BODY]]</div>
        </div>
        <div class="sidebar">
            <div style="background:var(--sidebar); padding:25px; border-radius:20px; border:1px solid #dadce0;">
                <h3 style="margin-top:0;">Route Specs</h3>
                <p><strong>Origin:</strong> [[COUNTRY_NAME]]</p>
                <p><strong>Dest:</strong> United States</p>
                <button onclick="window.print()" style="width:100%; padding:12px; background:var(--primary); color:white; border:none; border-radius:8px; font-weight:700; cursor:pointer;">Generate PDF Checklist</button>
            </div>
        </div>
    </div>
    <footer class="footer">© 2026 Pet Entry Guide. High-precision relocation data.</footer>
</body>
</html>
"""

# 2. 首页模板：Route Finder + 地理大区分类
INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pet Entry Guide | 2026 Route Finder & Policy Database</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lipis/flag-icons@7.0.0/css/flag-icons.min.css"/>
<style>
    :root { --primary: #1a73e8; --easy: #1e8e3e; --strict: #d93025; --standard: #f29900; --bg: #f8f9fa; }
    body { font-family: 'Inter', sans-serif; margin: 0; background: var(--bg); color: #202124; }
    
    /* Route Finder 区域 */
    .hero { background: white; padding: 80px 20px; text-align: center; border-bottom: 1px solid #dadce0; }
    h1 { font-size: 3.5em; letter-spacing: -0.05em; margin-bottom: 15px; color: #1a0dab; }
    .route-finder { max-width: 800px; margin: 30px auto; background: white; padding: 25px; border-radius: 50px; border: 1px solid #dfe1e5; display: flex; gap: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); align-items: center; justify-content: center; }
    select, input { border: none; font-size: 1.1em; outline: none; background: transparent; padding: 5px; cursor: pointer; }
    .divider { width: 1px; height: 30px; background: #eee; }
    .find-btn { background: var(--primary); color: white; padding: 12px 30px; border-radius: 30px; border: none; font-weight: 700; cursor: pointer; }

    .container { max-width: 1200px; margin: 50px auto; padding: 0 25px; }
    .region-section { margin-bottom: 60px; }
    .region-title { font-size: 1.8em; margin-bottom: 25px; display: flex; align-items: center; color: #5f6368; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; }
    
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(360px, 1fr)); gap: 30px; }
    
    /* 重构后的决策卡片 */
    .card { background: white; border: 1px solid #dadce0; border-radius: 20px; padding: 30px; text-decoration: none; color: inherit; transition: 0.3s; display: flex; flex-direction: column; }
    .card:hover { transform: translateY(-5px); box-shadow: 0 12px 30px rgba(0,0,0,0.08); border-color: var(--primary); }
    .card-tags { display: flex; gap: 8px; margin-bottom: 15px; }
    .tag { font-size: 0.75em; font-weight: 800; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; }
    
    h3 { margin: 0 0 12px; font-size: 1.4em; color: #1a73e8; }
    .summary { font-size: 1em; color: #5f6368; line-height: 1.5; font-weight: 500; }
    
    .footer { text-align: center; padding: 80px; color: #70757a; border-top: 1px solid #eee; }
</style>
</head>
<body>
<div class="hero">
    <h1>Pet Entry Guide</h1>
    <p style="font-size:1.4em; color:#5f6368;">2026 Professional Navigation for Global Pet Relocation.</p>
    
    <div class="route-finder">
        <span>From:</span>
        <input type="text" id="route-input" placeholder="Origin Country..." oninput="instantSearch(this.value)">
        <div class="divider"></div>
        <span>To:</span>
        <select disabled><option>United States (CDC/USDA)</option></select>
        <button class="find-btn">Find Protocol</button>
    </div>
</div>

<div class="container" id="main-content">
    <div class="region-section">
        <h2 class="region-title">Policy & Cost Insights</h2>
        <div class="grid">[[INSIGHT_CARDS]]</div>
    </div>
    
    [[REGION_SECTIONS]]
</div>

<script>
    function instantSearch(term) {
        const cards = document.querySelectorAll('.card');
        const sections = document.querySelectorAll('.region-section');
        const lowerTerm = term.toLowerCase();
        
        cards.forEach(card => {
            const match = card.innerText.toLowerCase().includes(lowerTerm);
            card.style.display = match ? 'flex' : 'none';
        });
        
        sections.forEach(sec => {
            const hasVisible = Array.from(sec.querySelectorAll('.card')).some(c => c.style.display !== 'none');
            sec.style.display = hasVisible ? 'block' : 'none';
        });
    }
</script>
</body>
</html>
"""

def main():
    # PM 重构：增加地理区域维度与政策分类
    regions = {
        'Asia-Pacific': ['china', 'japan', 'korea', 'south-korea', 'singapore', 'vietnam', 'thailand', 'philippines', 'india', 'taiwan', 'hongkong'],
        'Americas': ['canada', 'mexico', 'brazil', 'argentina'],
        'Europe': ['uk', 'eu', 'germany', 'france', 'italy', 'spain'],
        'Oceania': ['australia', 'nz']
    }
    
    country_codes = {'china': 'cn', 'japan': 'jp', 'south-korea': 'kr', 'korea': 'kr', 'singapore': 'sg', 'australia': 'au', 'canada': 'ca', 'uk': 'gb', 'mexico': 'mx', 'brazil': 'br', 'eu': 'eu'}

    if not os.path.exists('topics.csv'): return
    with open('topics.csv', 'r', encoding='utf-8') as f:
        rows = [r for r in list(csv.reader(f))[1:] if len(r) >= 2 and r[0].strip()]

    today = datetime.now().strftime('%b %d, %Y')
    
    # 初始化分组
    insight_cards = ""
    region_data = {region: [] for region in regions.keys()}
    region_data['Other Routes'] = [] # 虽然 PM 不建议，但逻辑上作为保底存在

    for slug, title, content in rows:
        # 识别文章类型
        is_insight = 'cost' in slug or 'general' in slug or 'cdc' in slug
        
        # 识别决策因子 (PM 方案：标签化)
        q_days = "0 Days" if "no quarantine" in content.lower() or "rabies-free" in content.lower() else "30-Day+"
        lead_time = "6-Month" if "rabies titer" in content.lower() else "30-Day"
        risk_level = "Strict" if q_days != "0 Days" else ("Standard" if "low-risk" in content.lower() else "Easy")
        tag_color = f'--{risk_level.lower()}'
        
        summary = "Requires CDC Permit & Official Microchip." if risk_level == "Strict" else "Streamlined entry with health certificate."
        
        # 生成详情页
        page_html = PAGE_TEMPLATE.replace('[[TITLE]]', title).replace('[[BODY]]', content).replace('[[TODAY]]', today)\
                     .replace('[[COUNTRY_NAME]]', slug.split('-')[0].capitalize())
        with open(f"{slug}.html", 'w', encoding='utf-8') as f_out: f_out.write(page_html)

        # 构建卡片 HTML (PM 方案：信息重组)
        card_html = f'''
        <a href="{slug}.html" class="card">
            <div class="card-tags">
                <span class="tag" style="background:var({tag_color}); color:white;">{risk_level}</span>
                <span class="tag" style="background:#eee; color:#666;">{lead_time} Lead</span>
                <span class="tag" style="background:#eee; color:#666;">{q_days} Quarantine</span>
            </div>
            <h3>{title.split('(')[0].strip()}</h3>
            <p class="summary">{summary}</p>
        </a>
        '''

        if is_insight:
            insight_cards += card_html
        else:
            origin = slug.split('-')[0]
            found_region = False
            for reg, countries in regions.items():
                if origin in countries:
                    region_data[reg].append(card_html)
                    found_region = True
                    break
            if not found_region:
                region_data['Other Routes'].append(card_html)

    # 组装首页大区
    region_sections_html = ""
    for reg, cards_list in region_data.items():
        if cards_list:
            # PM 方案：如果是 Other，检查是否有内容，尽量不显示这个标题
            display_title = reg if reg != 'Other Routes' else 'Additional Regions'
            region_sections_html += f'''
            <div class="region-section">
                <h2 class="region-title">{display_title}</h2>
                <div class="grid">{"".join(cards_list)}</div>
            </div>
            '''

    final_index = INDEX_TEMPLATE.replace('[[INSIGHT_CARDS]]', insight_cards).replace('[[REGION_SECTIONS]]', region_sections_html)
    with open('index.html', 'w', encoding='utf-8') as f_idx: f_idx.write(final_index)

if __name__ == "__main__":
    main()
