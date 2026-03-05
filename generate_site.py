import os
import json
import csv
from datetime import datetime

# ==========================================
# 1. 核心数据模型 (从 CSV 动态读取)
# ==========================================
def load_routes_from_csv(file_path="routes.csv"):
    routes = []
    if not os.path.exists(file_path):
        print(f"未能读取到数据源：{file_path}。请确保文件存在。")
        return routes
        
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # 逻辑：将 CSV 中的 "|" 分隔符拆分为渲染所需的列表，并提供默认容错值
            row['process_steps'] = row['process_steps'].split('|') if row.get('process_steps') else []
            row['required_documents'] = row['required_documents'].split('|') if row.get('required_documents') else []
            row['vaccines'] = row['vaccines'].split('|') if row.get('vaccines') else []
            row['tips'] = row['tips'].split('|') if row.get('tips') else []
            
            row['risk_level'] = row.get('risk_level', 'Standard')
            row['prep_time'] = row.get('prep_time', '30 Days')
            row['quarantine'] = row.get('quarantine', 'None')
            
            routes.append(row)
            
    return routes

# ==========================================
# 2. HTML 模板 (TailwindCSS)
# ==========================================
BASE_HTML_START = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | PetEntryGuide</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="https://petentryguide.com/{canonical_url}">
    <script src="https://cdn.tailwindcss.com"></script>
    {schema_json}
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }}
        details > summary {{ list-style: none; }}
        details > summary::-webkit-details-marker {{ display: none; }}
    </style>
</head>
<body class="bg-gray-50 text-gray-900">
    <nav class="bg-white border-b border-gray-200 py-4 px-6 sticky top-0 z-50 shadow-sm">
        <div class="max-w-5xl mx-auto flex justify-between items-center">
            <a href="/" class="text-xl font-extrabold text-blue-700 tracking-tight">PetEntryGuide</a>
            <div class="text-sm font-medium text-gray-500">2026 Database</div>
        </div>
    </nav>
"""

BASE_HTML_END = """
    <footer class="bg-white border-t border-gray-200 mt-16 py-12 text-center">
        <div class="max-w-3xl mx-auto px-6">
            <p class="text-sm text-gray-500 mb-4 font-medium">
                ⚠️ 当前规则基于 2026 年已知海关条例，政策存在随时调整概率，请在预订机票前通过官方渠道复核。
            </p>
            <p class="text-xs text-gray-400">&copy; 2026 PetEntryGuide. A Growth-Oriented Knowledge Base.</p>
        </div>
    </footer>
</body>
</html>
"""

# ==========================================
# 3. 页面生成逻辑
# ==========================================
def generate_schema(route):
    """注入 Schema.org 结构化数据以获取搜索引擎 Rich Snippets"""
    steps = [{"@type": "HowToStep", "text": step.split(': ')[-1] if ': ' in step else step} for step in route['process_steps']]
    schema = {"@context": "https://schema.org", "@type": "HowTo", "name": route['title'], "step": steps}
    return f'<script type="application/ld+json">\n{json.dumps(schema, indent=2)}\n</script>'

def generate_guide_page(route):
    """渲染仪表盘详情页并写入分层目录"""
    dest_dir = route['to_country'].strip().lower()
    origin_dir = f"from-{route['from_country'].strip().lower()}"
    pet_dir = route['pet_type'].strip().lower()
    
    canonical_url = f"{dest_dir}/{origin_dir}/{pet_dir}/"
    schema_script = generate_schema(route)
    
    risk_color = "bg-red-100 text-red-700 border-red-200" if "High" in route['risk_level'] else "bg-green-100 text-green-700 border-green-200"
    
    steps_html = ""
    for step in route['process_steps']:
        time_label, task = step.split(': ') if ': ' in step else ("Action", step)
        steps_html += f"""
        <div class="relative pl-8 mb-6">
            <div class="absolute left-0 top-1.5 w-3 h-3 bg-blue-500 rounded-full border-2 border-white ring-4 ring-blue-50"></div>
            <div class="text-sm font-bold text-blue-600 mb-1 uppercase tracking-wide">{time_label}</div>
            <label class="flex items-start space-x-3 cursor-pointer group">
                <input type="checkbox" class="peer mt-1 w-5 h-5 rounded border-gray-300 text-blue-600 focus:ring-blue-500 cursor-pointer">
                <span class="text-gray-800 text-lg peer-checked:line-through peer-checked:text-gray-400 transition-all">{task}</span>
            </label>
        </div>
        """
    
    docs_html = "".join([f'<li class="mb-2 flex items-center"><svg class="w-4 h-4 mr-2 text-green-500" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg>{doc}</li>' for doc in route['required_documents']])
    tips_html = "".join([f'<p class="mb-2">{tip}</p>' for tip in route['tips']])
    
    content = f"""
    <div class="max-w-3xl mx-auto px-6 py-8">
        <div class="mb-8">
            <div class="flex items-center space-x-2 text-sm text-gray-500 font-medium mb-4 uppercase">
                <a href="/">Home</a> <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
                <span>{route['from_country']}</span> <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                <span>{route['to_country']} ({route['pet_type']})</span>
            </div>
            
            <div class="flex flex-wrap gap-3 mb-6">
                <span class="px-3 py-1 rounded-md border text-sm font-bold {risk_color}">{route['risk_level']}</span>
                <span class="px-3 py-1 rounded-md border bg-gray-100 text-gray-700 text-sm font-bold">{route['prep_time']} Prep</span>
                <span class="px-3 py-1 rounded-md border bg-gray-100 text-gray-700 text-sm font-bold">Quarantine: {route['quarantine']}</span>
            </div>
            
            <h1 class="text-3xl font-extrabold text-gray-900 leading-tight mb-4">{route['title']}</h1>
        </div>

        <div class="bg-white p-8 rounded-2xl border border-gray-200 shadow-sm mb-8">
            <h2 class="text-2xl font-bold text-gray-900 mb-6 border-b pb-4">Timeline Checklist</h2>
            <div class="relative border-l-2 border-gray-100 ml-3 mt-4 space-y-2">{steps_html}</div>
        </div>

        <div class="space-y-4">
            <details class="group bg-white border border-gray-200 rounded-xl overflow-hidden [&_summary::-webkit-details-marker]:hidden">
                <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 text-gray-900 bg-gray-50 hover:bg-gray-100 transition">
                    Required Documents
                    <span class="transition group-open:rotate-180"><svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg></span>
                </summary>
                <div class="p-5 border-t border-gray-200 text-gray-700"><ul class="text-sm space-y-1">{docs_html}</ul></div>
            </details>
            <details class="group bg-white border border-gray-200 rounded-xl overflow-hidden [&_summary::-webkit-details-marker]:hidden">
                <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 text-gray-900 bg-gray-50 hover:bg-gray-100 transition">
                    Expert Policy Tips
                    <span class="transition group-open:rotate-180"><svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg></span>
                </summary>
                <div class="p-5 border-t border-gray-200 text-sm text-gray-700 bg-yellow-50">{tips_html}</div>
            </details>
        </div>
    </div>
    """
    
    html = BASE_HTML_START.format(title=route['title'], description=route.get('summary', ''), canonical_url=canonical_url, schema_json=schema_script) + content + BASE_HTML_END
    
    target_path = os.path.join("public", dest_dir, origin_dir, pet_dir)
    os.makedirs(target_path, exist_ok=True)
    with open(os.path.join(target_path, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

def generate_home_page(routes):
    """渲染首页及动态漏斗 (Route Selector)"""
    origins = sorted(list(set([r['from_country'].strip().lower() for r in routes])))
    dests = sorted(list(set([r['to_country'].strip().lower() for r in routes])))
    
    origin_opts = "".join([f'<option value="{o}">{o.capitalize()}</option>' for o in origins])
    dest_opts = "".join([f'<option value="{d}">To: {d.upper() if len(d)<=3 else d.capitalize()}</option>' for d in dests])
    
    cards_html = ""
    for route in routes[:9]:
        dest_dir, origin_dir, pet_dir = route['to_country'].strip().lower(), f"from-{route['from_country'].strip().lower()}", route['pet_type'].strip().lower()
        route_url = f"/{dest_dir}/{origin_dir}/{pet_dir}/"
        risk_color = "bg-red-50 text-red-700 border-red-200" if "High" in route['risk_level'] else "bg-green-50 text-green-700 border-green-200"
        
        cards_html += f"""
        <a href="{route_url}" class="block bg-white border border-gray-200 rounded-2xl p-6 hover:shadow-lg hover:border-blue-400 transition duration-200">
            <h3 class="text-xl font-extrabold text-gray-900 mb-4 uppercase">{route['from_country']} ➔ {route['to_country']} ({route['pet_type']})</h3>
            <div class="flex flex-col space-y-2">
                <span class="inline-flex items-center px-2.5 py-1 rounded-md text-xs font-bold border {risk_color} w-max">{route['risk_level']}</span>
                <span class="inline-flex items-center px-2.5 py-1 rounded-md text-xs font-bold bg-gray-100 text-gray-700 border border-gray-200 w-max">{route['prep_time']} Prep</span>
            </div>
        </a>
        """

    content = f"""
    <div class="bg-white border-b border-gray-200">
        <div class="max-w-4xl mx-auto px-6 py-20 text-center">
            <h1 class="text-5xl font-extrabold tracking-tight text-gray-900 mb-6">Route Finder</h1>
            <p class="text-xl text-gray-500 mb-10">Select origin and destination to generate your 2026 checklist.</p>
            
            <div class="bg-white p-3 rounded-2xl border border-gray-300 shadow-xl flex flex-col md:flex-row gap-3 items-center max-w-3xl mx-auto">
                <select id="sel-origin" class="flex-1 bg-gray-50 border border-gray-200 text-gray-700 text-lg font-medium rounded-xl px-4 py-3 outline-none">
                    <option value="" disabled selected>Select Origin</option>
                    {origin_opts}
                </select>
                <select id="sel-dest" class="flex-1 bg-gray-50 border border-gray-200 text-gray-700 text-lg font-medium rounded-xl px-4 py-3 outline-none">
                    {dest_opts}
                </select>
                <select id="sel-pet" class="flex-1 bg-gray-50 border border-gray-200 text-gray-700 text-lg font-medium rounded-xl px-4 py-3 outline-none">
                    <option value="dog">Pet: Dog</option>
                    <option value="cat">Pet: Cat</option>
                </select>
                <button onclick="getGuide()" class="w-full md:w-auto bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-8 rounded-xl cursor-pointer">Get Guide</button>
            </div>
        </div>
    </div>
    <div class="max-w-5xl mx-auto px-6 py-16">
        <h2 class="text-2xl font-bold text-gray-900 mb-8">Popular Routes</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">{cards_html}</div>
    </div>
    <script>
        function getGuide() {{
            const o = document.getElementById('sel-origin').value;
            const d = document.getElementById('sel-dest').value;
            const p = document.getElementById('sel-pet').value;
            if(o && d && p) window.location.href = '/' + d + '/from-' + o + '/' + p + '/';
        }}
    </script>
    """
    html = BASE_HTML_START.format(title="PetEntryGuide | Global Database", description="Structured pet import rules.", canonical_url="", schema_json="") + content + BASE_HTML_END
    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(html)

def generate_sitemap(routes):
    """输出符合层级路由规范的 sitemap"""
    urls = "<url><loc>https://petentryguide.com/</loc><priority>1.0</priority></url>\n"
    for route in routes:
        loc = f"https://petentryguide.com/{route['to_country'].strip().lower()}/from-{route['from_country'].strip().lower()}/{route['pet_type'].strip().lower()}/"
        urls += f"<url><loc>{loc}</loc><priority>0.8</priority></url>\n"
    sitemap = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>'
    with open("public/sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap)

# ==========================================
# 4. 执行控制与终极大扫除 (Nuclear Cleanup)
# ==========================================
if __name__ == "__main__":
    # --- 强行缝合迁徙逻辑 ---
    try:
        import migrate_data
        migrate_data.migrate() 
        print("Data migration successful!")
    except Exception as e:
        print(f"Migration skipped or failed: {e}")
    # -----------------------

    import glob
    import shutil
    # ... 后面的清理和生成代码保持不变 ...
