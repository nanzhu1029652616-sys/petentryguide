import csv
import os
import json
from datetime import datetime

# ----------------------------------------------------------------
# 1. 核心实体配置 (The Logic Engine)
# ----------------------------------------------------------------
COUNTRY_META = {
    'china': {'name': 'China', 'code': 'cn', 'risk': 'Standard'},
    'japan': {'name': 'Japan', 'code': 'jp', 'risk': 'Easy'},
    'south-korea': {'name': 'South Korea', 'code': 'kr', 'risk': 'Standard'},
    'australia': {'name': 'Australia', 'code': 'au', 'risk': 'Easy'},
    'uk': {'name': 'United Kingdom', 'code': 'gb', 'risk': 'Standard'},
    'mexico': {'name': 'Mexico', 'code': 'mx', 'risk': 'Standard'},
    'brazil': {'name': 'Brazil', 'code': 'br', 'risk': 'Strict'},
    'india': {'name': 'India', 'code': 'in', 'risk': 'Strict'},
    'usa': {'name': 'USA', 'code': 'us', 'risk': 'Dest'}
}

# ----------------------------------------------------------------
# 2. 终极指南页模板 (Guide Page - 保持上一次的精良设计)
# ----------------------------------------------------------------
GUIDE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[[TITLE]] | 2026 Pet Travel Expert</title>
    <script type="application/ld+json">[[SCHEMA]]</script>
    <style>
        :root { --primary: #1a73e8; --text: #202124; --bg: #f8f9fa; }
        body { font-family: 'Inter', -apple-system, sans-serif; color: var(--text); background: var(--bg); margin: 0; }
        .nav-bar { background: white; border-bottom: 1px solid #dadce0; padding: 15px 20px; position: sticky; top: 0; z-index: 100; font-size: 0.9em; }
        .nav-bar a { color: var(--primary); text-decoration: none; }
        .container { max-width: 1100px; margin: 30px auto; padding: 0 20px; display: grid; grid-template-columns: 1fr 320px; gap: 30px; }
        
        .dashboard-header { background: white; padding: 40px; border-radius: 24px; border: 1px solid #dadce0; grid-column: 1 / -1; }
        .route-info { font-size: 0.95em; color: #5f6368; margin-bottom: 20px; font-weight: 600; }
        h1 { margin: 0; font-size: 2.5em; letter-spacing: -0.02em; }
        .one-sentence-rule { background: #e8f0fe; color: #1967d2; padding: 15px 25px; border-radius: 12px; font-weight: 600; font-size: 1.1em; margin: 20px 0; border-left: 5px solid #1a73e8; }
        
        /* The Timeline */
        .timeline { margin: 40px 0 20px; position: relative; padding-left: 30px; }
        .time-step { position: relative; margin-bottom: 30px; }
        .time-step::before { content: ""; position: absolute; left: -30px; top: 5px; width: 12px; height: 12px; background: var(--primary); border-radius: 50%; }
        .time-step::after { content: ""; position: absolute; left: -25px; top: 25px; width: 2px; height: calc(100% + 5px); background: #eee; }
        .time-step:last-child::after { display: none; }
        .time-label { font-weight: 800; font-size: 0.85em; color: var(--primary); text-transform: uppercase; display: block; margin-bottom: 5px; }
        
        .main-content { background: white; padding: 40px; border-radius: 24px; border: 1px solid #dadce0; }
        .checklist h2 { margin-top: 0; }
        .todo-item { display: flex; align-items: flex-start; padding: 15px 0; border-bottom: 1px solid #f1f3f4; cursor: pointer; }
        .todo-item input { margin: 5px 15px 0 0; width: 20px; height: 20px; cursor: pointer; }
        .todo-item input:checked + span { text-decoration: line-through; color: #9aa0a6; }

        .cta-sidebar { background: var(--primary); color: white; padding: 30px; border-radius: 24px; position: sticky; top: 80px; text-align: center; }
        .cta-btn { width: 100%; padding: 15px; border-radius: 12px; border: none; font-weight: 700; font-size: 1.05em; cursor: pointer; margin-top: 15px; transition: 0.2s; }
        .cta-btn:hover { transform: translateY(-2px); }
        .footer { grid-column: 1 / -1; text-align: center; padding: 40px; color: #70757a; font-size: 0.9em; }
    </style>
</head>
<body>
    <div class="nav-bar">[[BREADCRUMBS]]</div>
    <div class="container">
        <div class="dashboard-header">
            <div class="route-info">Route: [[ORIGIN]] → [[DESTINATION]] &nbsp;|&nbsp; Pet: [[PET]] &nbsp;|&nbsp; Risk: [[RISK]]</div>
            <h1>[[TITLE]]</h1>
            <div class="one-sentence-rule">[[ONE_SENTENCE]]</div>
            
            <div class="timeline">
                <div class="time-step"><span class="time-label">T-6 Months</span><div>Rabies Vaccination & ISO Microchip</div></div>
                <div class="time-step"><span class="time-label">T-1 Month</span><div>Titer Test & CDC Import Form (if applicable)</div></div>
                <div class="time-step"><span class="time-label">T-7 Days</span><div>Government Health Certificate Endorsement</div></div>
                <div class="time-step"><span class="time-label">Arrival</span><div>Customs Declaration at Port of Entry</div></div>
            </div>
        </div>

        <div class="main-content">
            <div class="checklist">
                <h2>Interactive Checklist</h2>
                <label class="todo-item"><input type="checkbox"><span>ISO 11784/11785 Microchip</span></label>
                <label class="todo-item"><input type="checkbox"><span>Rabies Vaccination Certificate</span></label>
                <label class="todo-item"><input type="checkbox"><span>CDC Dog Import Form (Required 2026)</span></label>
                <label class="todo-item"><input type="checkbox"><span>Airline Approved Travel Crate</span></label>
            </div>
            <div style="margin-top:40px; padding-top:40px; border-top:1px solid #eee;">
                <h2>Detailed Regulations</h2>
                <div style="line-height:1.8; font-size:1.1em; color:#3c4043;">[[BODY]]</div>
            </div>
        </div>

        <aside class="sidebar">
            <div class="cta-sidebar">
                <h3 style="margin-top:0;">Need 1-on-1 Help?</h3>
                <p style="font-size:0.9em; opacity:0.9; margin-bottom:25px;">Avoid customs rejection. Have an expert handle your 2026 paperwork.</p>
                <button class="cta-btn" style="background:white; color:var(--primary);">Consult an Expert</button>
                <button class="cta-btn" onclick="window.print()" style="background:rgba(255,255,255,0.2); color:white;">Download PDF Guide</button>
            </div>
        </aside>
        <div class="footer">© 2026 Pet Entry Guide. High-precision relocation data.</div>
    </div>
</body>
</html>
"""

# ----------------------------------------------------------------
# 3. 首页模板 (PM 方案：一站式路径搜索 + Get My Guide CTA)
# ----------------------------------------------------------------
INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pet Entry Guide | 2026 Global Route Selector</title>
    <style>
        :root { --primary: #1a73e8; --bg: #f8f9fa; --text: #202124; }
        body { font-family: 'Inter', sans-serif; margin: 0; background: var(--bg); color: var(--text); }
        
        /* Hero Section & Trust Bar */
        .hero { background: white; padding: 100px 20px 80px; text-align: center; border-bottom: 1px solid #dadce0; }
        h1 { font-size: 3.8em; letter-spacing: -0.04em; color: #1a0dab; margin: 0 0 15px 0; }
        .trust-bar { display: inline-block; background: #e6f4ea; color: #1e8e3e; padding: 8px 16px; border-radius: 20px; font-weight: 600; font-size: 0.9em; margin-bottom: 40px; }
        
        /* Route Selector (核心 3 槽位) */
        .route-selector { max-width: 900px; margin: 0 auto; background: white; padding: 15px; border-radius: 60px; border: 1px solid #dfe1e5; display: flex; align-items: center; box-shadow: 0 10px 30px rgba(0,0,0,0.08); flex-wrap: wrap; }
        .selector-group { flex: 1; display: flex; flex-direction: column; text-align: left; padding: 0 25px; border-right: 1px solid #eee; min-width: 150px; }
        .selector-group:nth-child(3) { border-right: none; }
        .selector-label { font-size: 0.75em; text-transform: uppercase; font-weight: 700; color: #70757a; margin-bottom: 5px; }
        select { border: none; font-size: 1.1em; font-weight: 600; color: var(--text); outline: none; background: transparent; cursor: pointer; padding: 0; appearance: none; -webkit-appearance: none; }
        
        /* The CTA Button */
        .cta-btn { background: var(--primary); color: white; padding: 20px 40px; border-radius: 40px; border: none; font-weight: 800; font-size: 1.1em; cursor: pointer; transition: 0.2s; white-space: nowrap; margin-left: 10px; }
        .cta-btn:hover { background: #1557b0; transform: translateY(-2px); box-shadow: 0 4px 12px rgba(26,115,232,0.3); }

        /* Popular Routes Grid */
        .container { max-width: 1200px; margin: 60px auto; padding: 0 20px; }
        .section-title { font-size: 1.6em; margin-bottom: 30px; text-align: center; color: #5f6368; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 24px; }
        .card { background: white; border: 1px solid #dadce0; border-radius: 16px; padding: 25px; text-decoration: none; color: inherit; transition: 0.3s; }
        .card:hover { transform: translateY(-4px); box-shadow: 0 8px 20px rgba(0,0,0,0.06); border-color: var(--primary); }
        .card h3 { margin: 0 0 10px; color: var(--primary); font-size: 1.3em; }
        .card-tags { display: flex; gap: 8px; margin-bottom: 15px; }
        .card-tag { font-size: 0.75em; font-weight: 700; padding: 4px 8px; border-radius: 4px; background: #f1f3f4; color: #5f6368; }

        @media (max-width: 768px) {
            .route-selector { flex-direction: column; border-radius: 24px; padding: 20px; gap: 15px; }
            .selector-group { border-right: none; border-bottom: 1px solid #eee; padding: 10px 0; width: 100%; }
            .cta-btn { width: 100%; margin: 10px 0 0 0; }
        }
    </style>
</head>
<body>

<div class="hero">
    <h1>Global Pet Relocation</h1>
    <div class="trust-bar">✓ Verified 2026 Customs Data • Synchronized for 50+ Countries</div>
    
    <div class="route-selector">
        <div class="selector-group">
            <span class="selector-label">Origin</span>
            <select id="sel-origin">
                <option value="china">China</option>
                <option value="japan">Japan</option>
                <option value="australia">Australia</option>
                <option value="uk">United Kingdom</option>
                <option value="south-korea">South Korea</option>
                <option value="mexico">Mexico</option>
            </select>
        </div>
        <div class="selector-group">
            <span class="selector-label">Destination</span>
            <select id="sel-dest">
                <option value="usa">United States</option>
            </select>
        </div>
        <div class="selector-group">
            <span class="selector-label">Pet Type</span>
            <select id="sel-pet">
                <option value="dog">Dog</option>
                <option value="cat">Cat</option>
            </select>
        </div>
        <button class="cta-btn" onclick="getGuide()">Get My Guide</button>
    </div>
</div>

<div class="container">
    <h2 class="section-title">Popular Routes</h2>
    <div class="grid">
        [[POPULAR_CARDS]]
    </div>
</div>

<script>
    // JS 路由跳转逻辑：完美匹配后端的文件夹层级结构
    function getGuide() {
        const origin = document.getElementById('sel-origin').value;
        const dest = document.getElementById('sel-dest').value;
        const pet = document.getElementById('sel-pet').value;
        
        if(origin && dest && pet) {
            // 跳转到生成好的层级 URL
            window.location.href = '/' + dest + '/from-' + origin + '/' + pet + '.html';
        }
    }
</script>
</body>
</html>
"""

# ----------------------------------------------------------------
# 4. 生成与路由逻辑
# ----------------------------------------------------------------
def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def generate_schema(title, body):
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": title,
        "step": [
            {"@type": "HowToStep", "text": "Ensure ISO Microchip compliance."},
            {"@type": "HowToStep", "text": "Obtain Rabies vaccination certificate."},
            {"@type": "HowToStep", "text": "Submit Government Endorsed Forms."}
        ]
    })

def main():
    if not os.path.exists('topics.csv'): return
    with open('topics.csv', 'r', encoding='utf-8') as f:
        rows = [r for r in list(csv.reader(f))[1:] if len(r) >= 2]

    popular_cards_html = ""

    for slug, title, content in rows:
        # 跳过非标准航线（如 cost 或 general）
        if 'to' not in slug: continue
        
        parts = slug.split('-to-')
        if len(parts) < 2: continue
        
        origin_raw = parts[0]
        dest_pet = parts[1].split('-')
        dest_raw = dest_pet[0]
        pet_raw = dest_pet[1] if len(dest_pet) > 1 else 'pet'
        
        # 1. 创建层级目录
        dest_dir = dest_raw
        origin_dir = f"from-{origin_raw}"
        create_dir(f"{dest_dir}/{origin_dir}")
        
        # 2. 准备页面数据
        origin_name = COUNTRY_META.get(origin_raw, {}).get('name', origin_raw.capitalize())
        dest_name = COUNTRY_META.get(dest_raw, {}).get('name', dest_raw.upper())
        risk = COUNTRY_META.get(origin_raw, {}).get('risk', 'Standard')
        one_sentence = f"Traveling from {origin_name} to {dest_name} with a {pet_raw} is currently classified as {risk} Risk. Follow these essential steps."
        breadcrumbs = f'<a href="/">Route Finder</a> / <a href="#">{dest_name}</a> / {origin_name}'
        schema_json = generate_schema(title, content)
        
        # 3. 渲染详情页
        final_html = GUIDE_TEMPLATE.replace('[[TITLE]]', title)\
                                   .replace('[[BODY]]', content)\
                                   .replace('[[ORIGIN]]', origin_name)\
                                   .replace('[[DESTINATION]]', dest_name)\
                                   .replace('[[PET]]', pet_raw.capitalize())\
                                   .replace('[[RISK]]', risk)\
                                   .replace('[[ONE_SENTENCE]]', one_sentence)\
                                   .replace('[[BREADCRUMBS]]', breadcrumbs)\
                                   .replace('[[SCHEMA]]', schema_json)

        file_path = f"{dest_dir}/{origin_dir}/{pet_raw}.html"
        with open(file_path, 'w', encoding='utf-8') as f_out:
            f_out.write(final_html)

        # 4. 为首页生成卡片 (提取热门路径)
        if len(popular_cards_html) < 5000: # 限制首页只展示几个热门的
            q_days = "0 Days" if "no quarantine" in content.lower() else "Required"
            card_html = f'''
            <a href="/{file_path}" class="card">
                <div class="card-tags">
                    <span class="card-tag">{risk} Risk</span>
                    <span class="card-tag">{q_days} Quarantine</span>
                </div>
                <h3>{origin_name} to {dest_name} ({pet_raw.capitalize()})</h3>
                <p style="margin:0; font-size:0.9em; color:#5f6368;">View the full 2026 checklist and requirements...</p>
            </a>
            '''
            popular_cards_html += card_html

    # 5. 渲染并生成 index.html
    final_index = INDEX_TEMPLATE.replace('[[POPULAR_CARDS]]', popular_cards_html)
    with open('index.html', 'w', encoding='utf-8') as f_idx:
        f_idx.write(final_index)

    print("Success! Generated hierarchical URLs and Route Selector Home Page.")

if __name__ == "__main__":
    main()
