import csv
import os
from datetime import datetime

# 1. 文章详情页模板 (保持高级感)
PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Pet Entry Guide</title>
<meta name="description" content="{desc}">
<style>
    :root {{ --primary: #1a73e8; --text: #202124; --bg: #ffffff; --card-bg: #f8f9fa; }}
    body {{ 
        font-family: 'Inter', -apple-system, sans-serif; 
        line-height: 1.7; color: var(--text); background: var(--bg);
        max-width: 800px; margin: 0 auto; padding: 40px 20px; 
    }}
    h1 {{ font-size: 2.5em; color: var(--text); line-height: 1.2; margin-bottom: 20px; letter-spacing: -0.02em; }}
    .meta {{ font-size: 0.9em; color: #70757a; margin-bottom: 30px; border-bottom: 1px solid #eee; padding-bottom: 10px; }}
    .content {{ font-size: 1.1em; }}
    .content p {{ margin-bottom: 24px; }}
    .content strong {{ color: var(--primary); background: #e8f0fe; padding: 2px 6px; border-radius: 4px; font-weight: 600; }}
    .related-box {{ background: var(--card-bg); padding: 30px; border-radius: 12px; margin-top: 50px; border: 1px solid #dadce0; }}
    a {{ color: var(--primary); text-decoration: none; font-weight: 500; }}
    a:hover {{ text-decoration: underline; }}
    .footer {{ margin-top: 80px; font-size: 0.9em; color: #70757a; text-align: center; border-top: 1px solid #eee; padding-top: 40px; }}
</style>
</head>
<body>
    <h1>{title}</h1>
    <p class="meta">Expert Relocation Guide • Updated {today}</p>
    <div class="content">{article_body}</div>
    <div class="related-box">
        <h3>Keep Reading</h3>
        <ul>{related_links}</ul>
    </div>
    <div class="footer"><p>© 2026 Pet Entry Guide. Updated for March 2026.</p></div>
</body>
</html>
"""

# 2. 首页门户模板 (新增导航标签)
INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pet Entry Guide | 2026 USA Pet Travel Portal</title>
<style>
    :root {{ --primary: #1a73e8; --text: #202124; --bg: #f8f9fa; }}
    body {{ font-family: 'Inter', sans-serif; line-height: 1.6; color: var(--text); background: var(--bg); margin: 0; }}
    .hero {{ background: white; border-bottom: 1px solid #dadce0; padding: 60px 20px; text-align: center; }}
    .hero h1 {{ font-size: 3em; margin-bottom: 15px; color: #1a0dab; letter-spacing: -0.04em; }}
    
    /* 导航标签样式 */
    .nav-tags {{ 
        display: flex; justify-content: center; flex-wrap: wrap; 
        gap: 12px; margin: 30px auto; max-width: 900px; padding: 0 20px;
    }}
    .tag {{ 
        background: white; border: 1px solid #dadce0; padding: 8px 18px; 
        border-radius: 20px; text-decoration: none; color: #5f6368; 
        font-weight: 500; font-size: 0.95em; transition: 0.2s;
    }}
    .tag:hover {{ border-color: var(--primary); color: var(--primary); background: #e8f0fe; }}

    .container {{ max-width: 1200px; margin: 0 auto; padding: 0 25px 50px; }}
    .section-title {{ font-size: 1.8em; margin: 50px 0 25px; border-left: 5px solid var(--primary); padding-left: 15px; }}
    
    .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 25px; }}
    .card {{ 
        background: white; border: 1px solid #dadce0; border-radius: 16px; 
        padding: 28px; transition: 0.3s; text-decoration: none; color: inherit;
        display: flex; flex-direction: column; height: 100%; box-sizing: border-box;
    }}
    .card:hover {{ border-color: var(--primary); box-shadow: 0 10px 25px rgba(26,115,232,0.1); transform: translateY(-4px); }}
    .card h3 {{ margin: 0 0 12px 0; color: var(--primary); font-size: 1.25em; }}
    .card p {{ margin: 0; font-size: 0.9em; color: #5f6368; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }}
    
    .footer {{ text-align: center; padding: 60px; color: #70757a; }}
</style>
</head>
<body>
<div class="hero">
    <h1>Pet Entry Guide</h1>
    <p>2026 Expert Relocation Guides for your pet's journey to the USA.</p>
    <div class="nav-tags">{nav_tags}</div>
</div>
<div class="container">
    {content_sections}
</div>
<div class="footer"><p>© 2026 Pet Entry Guide. All guides are updated for current regulations.</p></div>
</body>
</html>
"""

def main():
    if not os.path.exists('topics.csv'): return

    # 国家映射表
    country_map = {
        'china': 'China', 'japan': 'Japan', 'korea': 'South Korea', 
        'singapore': 'Singapore', 'australia': 'Australia', 'canada': 'Canada',
        'uk': 'United Kingdom', 'eu': 'Europe', 'mexico': 'Mexico', 'usa': 'General/USA'
    }

    with open('topics.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = [r for r in reader if len(r) >= 2 and r[0].strip()]

    today = datetime.now().strftime('%b %d, %Y')
    
    # 按照国家对内容进行分组
    grouped_content = {}
    for slug, title, content in rows:
        # 从 slug 提取国家 (例如 "china-to-usa-cat" -> "china")
        first_part = slug.split('-')[0]
        country_name = country_map.get(first_part, 'Other Guides')
        
        if country_name not in grouped_content:
            grouped_content[country_name] = []
        
        clean_text = content.replace('<p>', '').replace('</p>', '').replace('<strong>', '').replace('</strong>', '')[:120] + "..."
        grouped_content[country_name].append({'slug': slug, 'title': title, 'content': content, 'snippet': clean_text})

        # 同时生成详情页
        html = PAGE_TEMPLATE.format(
            title=title, desc=clean_text[:150], today=today,
            article_body=content, related_links="".join([f'<li><a href="{r[0]}.html">{r[1]}</a></li>' for r in rows[:5]]),
            canonical=f"https://www.petentryguide.com/{slug}.html", year="2026"
        )
        with open(f'{slug}.html', 'w', encoding='utf-8') as f_out: f_out.write(html)

    # 构建首页导航标签和分组内容
    nav_tags = ""
    content_sections = ""
    
    # 按字母顺序排列国家
    sorted_countries = sorted(grouped_content.keys())
    for country in sorted_countries:
        anchor_id = country.lower().replace(' ', '-')
        nav_tags += f'<a href="#{anchor_id}" class="tag">{country}</a> '
        
        content_sections += f'<h2 class="section-title" id="{anchor_id}">{country}</h2><div class="grid">'
        for item in grouped_content[country]:
            content_sections += f'''
            <a href="{item['slug']}.html" class="card">
                <h3>{item['title']}</h3>
                <p>{item['snippet']}</p>
            </a>
            '''
        content_sections += '</div>'

    # 写入首页
    with open('index.html', 'w', encoding='utf-8') as f_idx:
        f_idx.write(INDEX_TEMPLATE.format(nav_tags=nav_tags, content_sections=content_sections))

    print(f"Success! Grouped {len(rows)} pages into {len(grouped_content)} countries.")

if __name__ == "__main__":
    main()
