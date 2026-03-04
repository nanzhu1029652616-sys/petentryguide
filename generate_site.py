import csv
import os
from datetime import datetime
import json # 新增：用于将数据安全传递给 JS

# 1. 文章详情页模板 (保持高级感)
PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Pet Entry Guide</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lipis/flag-icons@7.0.0/css/flag-icons.min.css"/>
<style>
    :root {{ --primary: #1a73e8; --text: #202124; --bg: #ffffff; --card-bg: #f8f9fa; }}
    body {{ 
        font-family: 'Inter', -apple-system, sans-serif; 
        line-height: 1.7; color: var(--text); background: var(--bg);
        max-width: 800px; margin: 0 auto; padding: 40px 20px; 
    }}
    .back-home {{ margin-bottom: 20px; display: inline-block; font-weight: 500; }}
    h1 {{ font-size: 2.5em; color: var(--text); line-height: 1.2; margin-bottom: 20px; letter-spacing: -0.02em; }}
    .meta {{ font-size: 0.9em; color: #70757a; margin-bottom: 30px; border-bottom: 1px solid #eee; padding-bottom: 10px; }}
    .content {{ font-size: 1.1em; }}
    .content p {{ margin-bottom: 24px; }}
    .content strong {{ color: var(--primary); background: #e8f0fe; padding: 2px 6px; border-radius: 4px; font-weight: 600; }}
    .fi {{ margin-right: 8px; border-radius: 2px; }} /* 国旗样式 */
    .related-box {{ background: var(--card-bg); padding: 30px; border-radius: 12px; margin-top: 50px; border: 1px solid #dadce0; }}
    a {{ color: var(--primary); text-decoration: none; font-weight: 500; }}
    a:hover {{ text-decoration: underline; }}
    .footer {{ margin-top: 80px; font-size: 0.9em; color: #70757a; text-align: center; border-top: 1px solid #eee; padding-top: 40px; }}
</style>
</head>
<body>
    <a href="/" class="back-home">← Back to Portal</a>
    <h1>{title}</h1>
    <p class="meta">Expert Relocation Guide • Updated {today}</p>
    <div class="content">{article_body}</div>
    <div class="footer"><p>© 2026 Pet Entry Guide. Information based on current 2026 travel regulations.</p></div>
</body>
</html>
"""

# 2. 首页门户模板 (新增导航标签、搜索和 JS 逻辑)
INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pet Entry Guide | 2026 USA Pet Travel Portal</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lipis/flag-icons@7.0.0/css/flag-icons.min.css"/>
<style>
    :root {{ --primary: #1a73e8; --text: #202124; --bg: #f8f9fa; }}
    body {{ font-family: 'Inter', sans-serif; line-height: 1.6; color: var(--text); background: var(--bg); margin: 0; padding: 0; }}
    .hero {{ background: white; border-bottom: 1px solid #dadce0; padding: 80px 20px; text-align: center; }}
    .hero h1 {{ font-size: 3.2em; margin-bottom: 15px; letter-spacing: -0.04em; color: #1a0dab; }}
    .hero p {{ font-size: 1.25em; color: #5f6368; max-width: 700px; margin: 0 auto; }}
    
    /* 搜索框样式 */
    .search-container {{ margin: 40px auto 0; max-width: 500px; position: relative; }}
    #search-input {{ 
        width: 100%; padding: 15px 25px 15px 50px; border: 1px solid #dadce0; 
        border-radius: 30px; font-size: 1.1em; box-shadow: 0 1px 6px rgba(32,33,36,0.1); 
        transition: 0.2s; box-sizing: border-box;
    }}
    #search-input:focus {{ outline: none; border-color: var(--primary); box-shadow: 0 1px 6px rgba(26,115,232,0.2); }}
    .search-icon {{ position: absolute; left: 20px; top: 50%; transform: translateY(-50%); color: #70757a; font-size: 1.2em; }}

    /* 导航标签样式 */
    .nav-tags {{ display: flex; justify-content: center; flex-wrap: wrap; gap: 10px; margin: 40px auto; max-width: 1000px; padding: 0 20px; }}
    .tag {{ 
        background: white; border: 1px solid #dadce0; padding: 8px 16px; border-radius: 20px; 
        text-decoration: none; color: #5f6368; font-weight: 500; font-size: 0.9em; 
        transition: 0.2s; display: flex; align-items: center; 
    }}
    .tag:hover {{ border-color: var(--primary); color: var(--primary); background: #e8f0fe; transform: translateY(-1px); }}
    .fi {{ margin-right: 6px; border-radius: 2px; }} /* 国旗样式 */

    .container {{ max-width: 1200px; margin: 0 auto; padding: 0 25px 50px; }}
    .section-title {{ font-size: 1.8em; margin: 60px 0 30px; border-left: 5px solid var(--primary); padding-left: 15px; display: flex; align-items: center; }}
    .section-title .fi {{ font-size: 0.8em; margin-right: 12px; }} /* 标题中国旗样式 */

    .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 25px; align-items: stretch; }}
    
    /* 卡片样式 */
    .card {{ 
        background: white; border: 1px solid #dadce0; border-radius: 16px; 
        padding: 28px; transition: 0.3s; text-decoration: none; color: inherit;
        display: flex; flex-direction: column; height: 100%; box-sizing: border-box; 
    }}
    .card:hover {{ border-color: var(--primary); box-shadow: 0 10px 25px rgba(26,115,232,0.1); transform: translateY(-4px); }}
    .card h3 {{ margin: 0 0 12px 0; color: var(--primary); font-size: 1.25em; }}
    .card p {{ margin: 0; font-size: 0.9em; color: #5f6368; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }}
    
    /* 搜索未找到的提示 */
    #no-results {{ text-align: center; color: #70757a; font-size: 1.2em; margin-top: 80px; display: none; }}

    .footer {{ text-align: center; padding: 80px; color: #70757a; border-top: 1px solid #dadce0; margin-top: 50px; background: white; }}
</style>
</head>
<body>
<div class="hero">
    <h1>Pet Entry Guide</h1>
    <p>DEFINITIVE 2026 Resource for Traveling with Pets to the United States.</p>
    
    <div class="search-container">
        <span class="search-icon">🔍</span>
        <input type="text" id="search-input" placeholder="Search guides (e.g., 'China dog', 'fees')...">
    </div>

    <div class="nav-tags">{nav_tags}</div>
</div>

<div class="container">
    <div id="content-sections">
        {content_sections}
    </div>
    
    <div id="no-results">No guides found matching your search. Try another term.</div>
</div>

<div class="footer"><p>© 2026 Pet Entry Guide. High-quality data for responsible pet owners.</p></div>

<script>
    const searchInput = document.getElementById('search-input');
    const sectionsContainer = document.getElementById('content-sections');
    const noResultsInfo = document.getElementById('no-results');
    const sectionTitles = document.querySelectorAll('.section-title');
    const grids = document.querySelectorAll('.grid');
    const cards = document.querySelectorAll('.card');

    searchInput.addEventListener('input', function() {{
        const searchTerm = this.value.toLowerCase().trim();
        let totalVisibleCards = 0;

        // 1. 如果搜索框为空，恢复所有内容
        if (searchTerm === '') {{
            sectionsContainer.style.display = 'block';
            noResultsInfo.style.display = 'none';
            sectionTitles.forEach(el => el.style.display = 'flex');
            grids.forEach(el => el.style.display = 'grid');
            cards.forEach(el => el.style.display = 'flex');
            return;
        }}

        // 2. 执行搜索过滤
        grids.forEach((grid, index) => {{
            let visibleCardsInGrid = 0;
            const currentGridCards = grid.querySelectorAll('.card');

            currentGridCards.forEach(card => {{
                // 获取卡片的标题和预览文字进行匹配
                const title = card.querySelector('h3').textContent.toLowerCase();
                const snippet = card.querySelector('p').textContent.toLowerCase();

                if (title.includes(searchTerm) || snippet.includes(searchTerm)) {{
                    card.style.display = 'flex';
                    visibleCardsInGrid++;
                    totalVisibleCards++;
                }} else {{
                    card.style.display = 'none';
                }}
            }});

            // 3. 根据网格内是否有可见卡片，显示/隐藏对应的国家标题和网格容器
            const titleId = grids[index].previousElementSibling.id;
            const correspondingTitle = document.getElementById(titleId);

            if (visibleCardsInGrid > 0) {{
                correspondingTitle.style.display = 'flex';
                grid.style.display = 'grid';
            }} else {{
                correspondingTitle.style.display = 'none';
                grid.style.display = 'none';
            }}
        }});

        // 4. 处理全站无结果的情况
        if (totalVisibleCards === 0) {{
            sectionsContainer.style.display = 'none';
            noResultsInfo.style.display = 'block';
        }} else {{
            sectionsContainer.style.display = 'block';
            noResultsInfo.style.display = 'none';
        }}
    }});
</script>

</body>
</html>
"""

def main():
    if not os.path.exists('topics.csv'): return

    # 国家/地区映射表 (包含国家代码用于图标)
    country_map = {{
        'china': {{'name': 'China', 'code': 'cn'}},
        'japan': {{'name': 'Japan', 'code': 'jp'}},
        'korea': {{'name': 'South Korea', 'code': 'kr'}},
        'singapore': {{'name': 'Singapore', 'code': 'sg'}},
        'australia': {{'name': 'Australia', 'code': 'au'}},
        'canada': {{'name': 'Canada', 'code': 'ca'}},
        'uk': {{'name': 'United Kingdom', 'code': 'gb'}}, # 'gb' for UK
        'eu': {{'name': 'Europe', 'code': 'eu'}},
        'mexico': {{'name': 'Mexico', 'code': 'mx'}},
        'brazil': {{'name': 'Brazil', 'code': 'br'}},
        'india': {{'name': 'India', 'code': 'in'}},
        'philippines': {{'name': 'Philippines', 'code': 'ph'}},
        'thailand': {{'name': 'Thailand', 'code': 'th'}},
        'vietnam': {{'name': 'Vietnam', 'code': 'vn'}},
        'malaysia': {{'name': 'Malaysia', 'code': 'my'}},
        'taiwan': {{'name': 'Taiwan', 'code': 'tw'}},
        'hongkong': {{'name': 'Hong Kong', 'code': 'hk'}},
        'usa': {{'name': 'General/USA', 'code': 'us'}}
    }}

    with open('topics.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        # 增加过滤：只有 slug 和 title 都有内容的行才保留
        rows = [r for r in reader if len(r) >= 2 and r[0].strip() and r[1].strip()]

    today = datetime.now().strftime('%b %d, %Y')
    
    # 按照国家对内容进行分组
    grouped_content = {{}}
    for slug, title, content in rows:
        # 从 slug 提取国家 (例如 "china-to-usa-cat" -> "china")
        first_part = slug.split('-')[0]
        country_info = country_map.get(first_part, {{'name': 'Other Guides', 'code': '🏳️'}} ) # 默认图标
        
        country_name = country_info['name']
        country_code = country_info['code']

        if country_name not in grouped_content:
            grouped_content[country_name] = {{'code': country_code, 'items': []}}
        
        # 截取正文前120字作为首页预览
        clean_text = content.replace('<p>', '').replace('</p>', '').replace('<strong>', '').replace('</strong>', '').replace('<ul>', '').replace('<li>', '').replace('</li>', '').replace('</ul>', '')
        snippet = clean_text[:120] + "..."
        grouped_content[country_name]['items'].append({{'slug': slug, 'title': title, 'content': content, 'snippet': snippet}})

        # 同时生成详情页
        html = PAGE_TEMPLATE.format(
            title=title,
            desc=clean_text[:150],
            today=today,
            article_body=content,
            related_links="".join([f'<li><a href="{{r[0]}}.html">{{r[1]}}</a></li>' for r in rows[:5]]),
            canonical=f"https://www.petentryguide.com/{{slug}}.html",
            year="2026"
        )
        with open(f'{{slug}}.html', 'w', encoding='utf-8') as f_out:
            f_out.write(html)

    # 构建首页导航标签和分组内容
    nav_tags = ""
    content_sections = ""
    
    # 按字母顺序排列国家 (General/USA排在最前)
    sorted_countries = sorted(grouped_content.keys())
    if 'General/USA' in sorted_countries:
        sorted_countries.remove('General/USA')
        sorted_countries.insert(0, 'General/USA')

    for country in sorted_countries:
        info = grouped_content[country]
        code = info['code']
        anchor_id = country.lower().replace(' ', '-').replace('/', '-')
        
        # 生成带图标的导航标签
        nav_tags += f'<a href="#{{anchor_id}}" class="tag"><span class="fi fi-{{code}}"></span>{{country}}</a> '
        
        # 生成带图标的国家标题和网格
        content_sections += f'''
        <h2 class="section-title" id="{{anchor_id}}">
            <span class="fi fi-{{code}}"></span>
            {{country}}
        </h2>
        <div class="grid">
        '''
        
        for item in info['items']:
            content_sections += f'''
            <a href="{{item['slug']}}.html" class="card">
                <h3>{{item['title']}}</h3>
                <p>{{item['snippet']}}</p>
            </a>
            '''
        content_sections += '</div>' # 闭合 grid

    # 写入首页
    with open('index.html', 'w', encoding='utf-8') as f_idx:
        f_idx.write(INDEX_TEMPLATE.format(nav_tags=nav_tags, content_sections=content_sections))

    print(f"Success! Re-engineered portal with search and flags. Processed {{len(rows)}} pages.")

if __name__ == "__main__":
    main()
