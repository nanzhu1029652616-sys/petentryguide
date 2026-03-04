import csv
import os
from datetime import datetime

# 1. 文章详情页模板
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
    .related-box h3 {{ margin-top: 0; }}
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
    <div class="footer">
        <p>© 2026 Pet Entry Guide. Information based on current 2026 travel regulations.</p>
    </div>
</body>
</html>
"""

# 2. 首页门户模板 (修复了卡片对齐问题)
INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pet Entry Guide | 2026 USA Pet Travel Portal</title>
<style>
    :root {{ --primary: #1a73e8; --text: #202124; --bg: #f8f9fa; }}
    body {{ font-family: 'Inter', sans-serif; line-height: 1.6; color: var(--text); background: var(--bg); margin: 0; }}
    .hero {{ background: white; border-bottom: 1px solid #dadce0; padding: 80px 20px; text-align: center; }}
    .hero h1 {{ font-size: 3.2em; margin-bottom: 15px; letter-spacing: -0.04em; color: #1a0dab; }}
    .hero p {{ font-size: 1.25em; color: #5f6368; max-width: 700px; margin: 0 auto; }}
    
    .container {{ max-width: 1200px; margin: 50px auto; padding: 0 25px; }}
    
    /* 核心修复：网格对齐 */
    .grid {{ 
        display: grid; 
        grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); 
        gap: 25px;
        align-items: stretch; /* 强制所有卡片拉伸到同一高度 */
    }}
    
    .card {{ 
        background: white; border: 1px solid #dadce0; border-radius: 16px; 
        padding: 28px; transition: 0.3s cubic-bezier(0.4, 0, 0.2, 1); 
        text-decoration: none; color: inherit;
        display: flex; flex-direction: column;
        height: 100%; /* 关键修复 */
        box-sizing: border-box;
    }}
    .card:hover {{ 
        border-color: var(--primary); 
        box-shadow: 0 10px 25px rgba(26,115,232,0.12); 
        transform: translateY(-4px); 
    }}
    .card h3 {{ margin: 0 0 12px 0; color: var(--primary); font-size: 1.3em; line-height: 1.3; }}
    
    /* 核心修复：预览文字行数限制 */
    .card p {{ 
        margin: 0; font-size: 0.95em; color: #5f6368; 
        display: -webkit-box;
        -webkit-line-clamp: 3; /* 只显示3行 */
        -webkit-box-orient: vertical;
        overflow: hidden;
        text-overflow: ellipsis;
    }}
    
    .footer {{ text-align: center; padding: 60px 20px; color: #70757a; font-size: 0.95em; }}
</style>
</head>
<body>
<div class="hero">
    <h1>Pet Entry Guide</h1>
    <p>The definitive 2026 resource for traveling with your furry companions to the United States.</p>
</div>
<div class="container">
    <div class="grid">{index_items}</div>
</div>
<div class="footer"><p>© 2026 Pet Entry Guide. All guides are updated for March 2026.</p></div>
</body>
</html>
"""

def main():
    if not os.path.exists('topics.csv'): return

    with open('topics.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        # 增加过滤：只有 slug 和 title 都有内容的行才保留
        rows = [r for r in reader if len(r) >= 2 and r[0].strip() and r[1].strip()]

    today = datetime.now().strftime('%b %d, %Y')
    index_items = ""

    for slug, title, content in rows:
        # 生成首页卡片
        clean_text = content.replace('<p>', '').replace('</p>', '').replace('<strong>', '').replace('</strong>', '').replace('<ul>', '').replace('<li>', '').replace('</li>', '').replace('</ul>', '')
        index_items += f'''
        <a href="{slug}.html" class="card">
            <h3>{title}</h3>
            <p>{clean_text}</p>
        </a>
        '''

        # 生成详情页
        related = ""
        # 随机取几个作为相关推荐
        for s, t, c in rows[:6]:
            if s != slug: related += f'<li><a href="{s}.html">{t}</a></li>'

        html = PAGE_TEMPLATE.format(
            title=title,
            desc=clean_text[:150],
            today=today,
            article_body=content,
            related_links=related,
            canonical=f"https://www.petentryguide.com/{slug}.html",
            year="2026"
        )
        with open(f'{slug}.html', 'w', encoding='utf-8') as f_out:
            f_out.write(html)

    # 写入首页
    with open('index.html', 'w', encoding='utf-8') as f_idx:
        f_idx.write(INDEX_TEMPLATE.format(index_items=index_items))

    print(f"Success! Re-designed {len(rows)} pages with consistent layout.")

if __name__ == "__main__":
    main()
