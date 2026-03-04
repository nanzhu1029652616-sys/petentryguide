import csv
import os
from datetime import datetime

# 1. 文章详情页模板 (转义了大括号以支持 CSS)
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
        max-width: 760px; margin: 0 auto; padding: 40px 20px; 
    }}
    h1 {{ font-size: 2.2em; color: var(--text); line-height: 1.2; margin-bottom: 8px; }}
    .meta {{ font-size: 0.9em; color: #70757a; margin-bottom: 30px; }}
    .content {{ 
        background: var(--bg); border: 1px solid #dadce0; border-radius: 12px; 
        padding: 32px; margin: 24px 0; box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }}
    .content strong {{ color: var(--primary); background: #e8f0fe; padding: 0 4px; border-radius: 4px; }}
    .related-box {{ background: var(--card-bg); padding: 24px; border-radius: 8px; margin-top: 40px; }}
    a {{ color: var(--primary); text-decoration: none; font-weight: 500; }}
    .footer {{ margin-top: 60px; font-size: 0.85em; color: #70757a; text-align: center; border-top: 1px solid #eee; padding-top: 30px; }}
</style>
</head>
<body>
<h1>{title}</h1>
<p class="meta">Updated: {today} • 2026 Guide</p>
<div class="content">{article_body}</div>
<div class="related-box">
    <h3>Essential Resources</h3>
    <ul>{related_links}</ul>
</div>
<div class="footer"><p>© 2026 Pet Entry Guide. All rights reserved.</p></div>
</body>
</html>
"""

# 2. 首页门户模板
INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pet Entry Guide | 2026 International Pet Travel Portal</title>
<style>
    :root {{ --primary: #1a73e8; --text: #202124; --bg: #f8f9fa; }}
    body {{ font-family: 'Inter', sans-serif; line-height: 1.6; color: var(--text); background: var(--bg); margin: 0; }}
    .hero {{ background: white; border-bottom: 1px solid #dadce0; padding: 60px 20px; text-align: center; }}
    .hero h1 {{ font-size: 2.8em; margin-bottom: 10px; }}
    .container {{ max-width: 1100px; margin: 40px auto; padding: 0 20px; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; }}
    .card {{ 
        background: white; border: 1px solid #dadce0; border-radius: 12px; 
        padding: 24px; transition: 0.2s; text-decoration: none; color: inherit;
        display: flex; flex-direction: column;
    }}
    .card:hover {{ border-color: var(--primary); box-shadow: 0 4px 12px rgba(26,115,232,0.1); transform: translateY(-2px); }}
    .card h3 {{ margin: 0 0 10px 0; color: var(--primary); }}
    .card p {{ margin: 0; font-size: 0.9em; color: #5f6368; }}
</style>
</head>
<body>
<div class="hero">
    <h1>Pet Entry Guide</h1>
    <p>2026 Expert Relocation Guides for your pet's journey to the USA.</p>
</div>
<div class="container">
    <div class="grid">{index_items}</div>
</div>
</body>
</html>
"""

def main():
    if not os.path.exists('topics.csv'):
        print("Error: topics.csv not found")
        return

    with open('topics.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)

    today = datetime.now().strftime('%Y-%m-%d')
    index_items = ""

    # 生成各篇文章
    for slug, title, content in rows:
        if not slug or not title: continue
        
        # 为首页生成卡片内容 (截取正文前80字作为预览)
        snippet = content.replace('<p>', '').replace('</p>', '').replace('<strong>', '').replace('</strong>', '')[:80] + "..."
        index_items += f'''
        <a href="{slug}.html" class="card">
            <h3>{title}</h3>
            <p>{snippet}</p>
        </a>
        '''

        # 生成详情页链接列表
        related = ""
        for s, t, c in rows[:5]: # 随便展示前5个作为相关阅读
            related += f'<li><a href="{s}.html">{t}</a></li>'

        # 写入详情页
        html = PAGE_TEMPLATE.format(
            title=title,
            desc=snippet,
            today=today,
            article_body=content,
            related_links=related,
            canonical=f"https://www.petentryguide.com/{slug}.html",
            year="2026"
        )
        with open(f'{slug}.html', 'w', encoding='utf-8') as f_out:
            f_out.write(html)

    # 生成首页
    with open('index.html', 'w', encoding='utf-8') as f_idx:
        f_idx.write(INDEX_TEMPLATE.format(index_items=index_items))

    print(f"Success! Processed {len(rows)} pages.")

if __name__ == "__main__":
    main()
