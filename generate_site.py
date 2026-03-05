import os
import json
import csv
import glob
import shutil
from datetime import datetime

# ==========================================
# 1. 核心逻辑：数据加载
# ==========================================
def load_routes_from_csv(file_path="routes.csv"):
    routes = []
    if not os.path.exists(file_path): return routes
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # 列表化处理
            for key in ['process_steps', 'required_documents', 'tips']:
                row[key] = row.get(key, '').split('|') if row.get(key) else []
            row['risk_level'] = row.get('risk_level', 'Standard')
            row['prep_time'] = row.get('prep_time', '30 Days')
            routes.append(row)
    return routes

# ==========================================
# 2. HTML 模板
# ==========================================
BASE_HTML_START = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | PetEntryGuide</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="https://petentryguide.com/{canonical_url}">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>body {{ font-family: sans-serif; }}</style>
</head>
<body class="bg-gray-50 text-gray-900">
    <nav class="bg-white border-b py-4 px-6 sticky top-0 z-50 shadow-sm">
        <div class="max-w-5xl mx-auto flex justify-between items-center">
            <a href="/" class="text-xl font-extrabold text-blue-700">PetEntryGuide</a>
            <div class="text-sm font-medium text-gray-500">2026 Database</div>
        </div>
    </nav>
"""
BASE_HTML_END = """<footer class="mt-16 py-12 text-center border-t text-sm text-gray-400">&copy; 2026 PetEntryGuide.</footer></body></html>"""

# ==========================================
# 3. 页面生成逻辑
# ==========================================
def generate_guide_page(route):
    dest, origin, pet = route['to_country'].lower(), f"from-{route['from_country'].lower()}", route['pet_type'].lower()
    canonical_url = f"{dest}/{origin}/{pet}/"
    
    # --- 核心修复点：使用 split(': ', 1) 确保只切分一次，防止冒号过多报错 ---
    steps_html = ""
    for step in route['process_steps']:
        if not step.strip(): continue
        label, task = step.split(': ', 1) if ': ' in step else ("Action", step)
        steps_html += f'''
        <div class="relative pl-8 mb-6">
            <div class="absolute left-0 top-1.5 w-3 h-3 bg-blue-500 rounded-full"></div>
            <div class="text-sm font-bold text-blue-600 mb-1">{label}</div>
            <label class="flex items-start space-x-3 cursor-pointer">
                <input type="checkbox" class="peer mt-1">
                <span class="peer-checked:line-through peer-checked:text-gray-400">{task}</span>
            </label>
        </div>'''

    content = f"""
    <div class="max-w-3xl mx-auto px-6 py-8">
        <h1 class="text-3xl font-extrabold mb-6">{route['title']}</h1>
        <div class="bg-white p-8 rounded-2xl border shadow-sm mb-8">
            <h2 class="text-2xl font-bold mb-6 border-b pb-4">Timeline Checklist</h2>
            <div class="relative border-l-2 border-gray-100 ml-3 mt-4 space-y-2">{steps_html}</div>
        </div>
    </div>"""
    
    html = BASE_HTML_START.format(title=route['title'], description=route.get('summary', ''), canonical_url=canonical_url, schema_json="") + content + BASE_HTML_END
    target = os.path.join("public", dest, origin, pet)
    os.makedirs(target, exist_ok=True)
    with open(os.path.join(target, "index.html"), "w", encoding="utf-8") as f: f.write(html)

def generate_home_page(routes):
    origins = sorted(list(set([r['from_country'].lower() for r in routes])))
    dests = sorted(list(set([r['to_country'].lower() for r in routes])))
    origin_opts = "".join([f'<option value="{o}">{o.capitalize()}</option>' for o in origins])
    dest_opts = "".join([f'<option value="{d}">To: {d.capitalize()}</option>' for d in dests])
    
    cards_html = ""
    for route in routes[:12]:
        url = f"/{route['to_country'].lower()}/from-{route['from_country'].lower()}/{route['pet_type'].lower()}/"
        cards_html += f'''
        <a href="{url}" class="block bg-white border rounded-2xl p-6 hover:shadow-lg">
            <h3 class="font-bold">{route["from_country"]} ➔ {route["to_country"]}</h3>
            <p class="text-sm text-gray-500">{route["risk_level"]} | {route["prep_time"]}</p>
        </a>'''

    content = f"""
    <div class="max-w-4xl mx-auto px-6 py-20 text-center">
        <h1 class="text-5xl font-extrabold mb-10 tracking-tight">Route Finder</h1>
        <div class="bg-white p-3 rounded-2xl border shadow-xl flex flex-col md:flex-row gap-3 items-center max-w-3xl mx-auto">
            <select id="sel-origin" class="flex-1 bg-gray-50 border rounded-xl px-4 py-3"><option value="" disabled selected>Origin</option>{origin_opts}</select>
            <select id="sel-dest" class="flex-1 bg-gray-50 border rounded-xl px-4 py-3">{dest_opts}</select>
            <select id="sel-pet" class="flex-1 bg-gray-50 border rounded-xl px-4 py-3"><option value="dog">Dog</option><option value="cat">Cat</option></select>
            <button onclick="getGuide()" class="bg-blue-600 text-white font-bold py-3 px-8 rounded-xl cursor-pointer">Get Guide</button>
        </div>
    </div>
    <div class="max-w-5xl mx-auto px-6 py-16"><div class="grid md:grid-cols-3 gap-6">{cards_html}</div></div>
    <script>function getGuide(){{const o=document.getElementById('sel-origin').value,d=document.getElementById('sel-dest').value,p=document.getElementById('sel-pet').value; if(o&&d&&p) window.location.href='/'+d+'/from-'+o+'/'+p+'/';}}</script>"""
    html = BASE_HTML_START.format(title="PetEntryGuide", description="Database", canonical_url="", schema_json="") + content + BASE_HTML_END
    with open("public/index.html", "w", encoding="utf-8") as f: f.write(html)

def generate_sitemap(routes):
    urls = "<url><loc>https://petentryguide.com/</loc><priority>1.0</priority></url>\\n"
    for r in routes:
        loc = f"https://petentryguide.com/{r['to_country'].lower()}/from-{r['from_country'].lower()}/{r['pet_type'].lower()}/"
        urls += f"<url><loc>{loc}</loc></url>\\n"
    with open("public/sitemap.xml", "w", encoding="utf-8") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')

if __name__ == "__main__":
    # 1. 清理
    print("🧹 清理旧文件...")
    for f in glob.glob("*.html"): os.remove(f)
    junk = ['app', 'book', 'components', 'fly', 'lib', 'usa', 'data/routes']
    for j in junk:
        if os.path.exists(j): 
            if os.path.isdir(j): shutil.rmtree(j)
            else: os.remove(j)

    # 2. 迁徙数据
    print("🚢 正在迁徙旧数据...")
    try:
        import migrate_data
        migrate_data.migrate()
    except Exception as e: print(f"❌ 迁徙跳过: {e}")

    # 3. 生成
    routes_data = load_routes_from_csv("routes.csv")
    if routes_data:
        if not os.path.exists("public"): os.makedirs("public")
        generate_home_page(routes_data)
        for route in routes_data: generate_guide_page(route)
        generate_sitemap(routes_data)
        print(f"🚀 构建成功！已处理 {len(routes_data)} 条路线。")
    else: print("❌ 错误：无数据。")
