import os
import json
import csv  # 新增事实：导入 Python 内置的 csv 模块
from datetime import datetime

# ==========================================
# 1. 核心数据模型 (从 CSV 动态读取)
# ==========================================
def load_routes_from_csv(file_path="routes.csv"):
    """逻辑：读取外部 CSV 文件，并将特定字段还原为列表"""
    routes = []
    
    if not os.path.exists(file_path):
        print(f"警告：未找到数据源 {file_path}")
        return routes
        
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # 核心逻辑：将 CSV 中用 "|" 分隔的纯文本字符串，拆分成 HTML 渲染需要的列表 (List)
            row['process_steps'] = row['process_steps'].split('|') if row['process_steps'] else []
            row['required_documents'] = row['required_documents'].split('|') if row['required_documents'] else []
            row['vaccines'] = row['vaccines'].split('|') if row['vaccines'] else []
            row['travel_methods'] = row['travel_methods'].split('|') if row['travel_methods'] else []
            row['tips'] = row['tips'].split('|') if row['tips'] else []
            
            routes.append(row)
            
    return routes

# 执行读取操作，ROUTES_DATA 现在由外部表格驱动
ROUTES_DATA = load_routes_from_csv()

# ==========================================
# 2. HTML 模板 (TailwindCSS 架构)
# ==========================================

BASE_HTML_START = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="https://petentryguide.com/{slug}">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
    </style>
</head>
<body class="bg-gray-50 text-gray-900">
    <nav class="bg-white border-b border-gray-200 py-4 px-6 sticky top-0 z-50">
        <div class="max-w-5xl mx-auto flex justify-between items-center">
            <a href="/" class="text-xl font-bold text-blue-600">PetEntryGuide</a>
            <div class="text-sm text-gray-500">2026 Import Requirements</div>
        </div>
    </nav>
"""

BASE_HTML_END = """
    <footer class="bg-white border-t border-gray-200 mt-20 py-10 text-center text-sm text-gray-500">
        <div class="max-w-5xl mx-auto">
            &copy; 2026 PetEntryGuide. All information is for guidance purposes. Check official sources.
        </div>
    </footer>
</body>
</html>
"""

# ==========================================
# 3. 页面生成逻辑
# ==========================================

def generate_guide_page(route):
    """生成详情页"""
    
    # 渲染步骤
    steps_html = ""
    for idx, step in enumerate(route['process_steps']):
        steps_html += f'<li class="mb-4 flex"><span class="font-bold text-blue-600 mr-3">Step {idx+1}</span> <span>{step}</span></li>'
    
    # 渲染文档
    docs_html = "".join([f'<li class="list-disc ml-5 mb-2">{doc}</li>' for doc in route['required_documents']])
    
    # 渲染提示
    tips_html = "".join([f'<p class="text-yellow-800 font-medium">{tip}</p>' for tip in route['tips']])
    
    content = f"""
    <div class="max-w-4xl mx-auto px-6 py-10">
        <div class="text-sm text-gray-500 mb-6">
            <a href="/" class="hover:text-blue-600">Home</a> > {route['from_country']} > {route['to_country']} > {route['pet_type'].capitalize()}
        </div>

        <h1 class="text-4xl font-extrabold tracking-tight text-gray-900 mb-4">{route['title']}</h1>
        <p class="text-lg text-gray-600 mb-10">{route['summary']}</p>

        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-12">
            <div class="bg-white p-5 rounded-xl border border-gray-200 shadow-sm">
                <div class="text-xs text-gray-500 uppercase font-semibold mb-1">Minimum Age</div>
                <div class="font-bold text-gray-900">{route['min_age']}</div>
            </div>
            <div class="bg-white p-5 rounded-xl border border-gray-200 shadow-sm">
                <div class="text-xs text-gray-500 uppercase font-semibold mb-1">Microchip</div>
                <div class="font-bold text-gray-900">{route['microchip']}</div>
            </div>
            <div class="bg-white p-5 rounded-xl border border-gray-200 shadow-sm">
                <div class="text-xs text-gray-500 uppercase font-semibold mb-1">Rabies</div>
                <div class="font-bold text-gray-900">{route['rabies_vaccine']}</div>
            </div>
            <div class="bg-white p-5 rounded-xl border border-gray-200 shadow-sm">
                <div class="text-xs text-gray-500 uppercase font-semibold mb-1">Quarantine</div>
                <div class="font-bold text-gray-900">{route['quarantine']}</div>
            </div>
        </div>

        <div class="grid md:grid-cols-3 gap-10">
            <div class="md:col-span-2">
                <h2 class="text-2xl font-bold border-b pb-2 mb-6">Step-by-Step Process</h2>
                <ul class="mb-10 text-gray-700">{steps_html}</ul>

                <h2 class="text-2xl font-bold border-b pb-2 mb-6">Required Documents</h2>
                <ul class="mb-10 text-gray-700">{docs_html}</ul>
            </div>

            <div>
                <div class="bg-yellow-50 border-l-4 border-yellow-400 p-5 rounded-r-lg mb-8">
                    <h3 class="font-bold text-yellow-800 mb-2">Expert Tips</h3>
                    {tips_html}
                </div>
            </div>
        </div>
    </div>
    """
    
    html = BASE_HTML_START.format(title=route['title'], description=route['summary'], slug=route['slug']) + content + BASE_HTML_END
    
    with open(f"public/{route['slug']}.html", "w", encoding="utf-8") as f:
        f.write(html)

def generate_home_page():
    """生成带有三槽位搜索的首页"""
    cards_html = ""
    for route in ROUTES_DATA:
        cards_html += f"""
        <a href="/{route['slug']}.html" class="block bg-white border border-gray-200 rounded-xl p-6 hover:shadow-md hover:border-blue-500 transition">
            <div class="text-sm font-semibold text-blue-600 mb-2 uppercase tracking-wide">{route['pet_type']} GUIDE</div>
            <h3 class="text-xl font-bold mb-2">{route['from_country']} → {route['to_country']}</h3>
            <p class="text-gray-600 text-sm">{route['summary']}</p>
        </a>
        """

    content = f"""
    <div class="bg-white border-b border-gray-200">
        <div class="max-w-4xl mx-auto px-6 py-20 text-center">
            <h1 class="text-5xl font-extrabold tracking-tight text-gray-900 mb-6">Find Pet Import Requirements Worldwide</h1>
            <p class="text-xl text-gray-500 mb-10">Search official import rules for traveling internationally with pets.</p>
            
            <div class="bg-white p-4 rounded-full border border-gray-300 shadow-lg flex flex-col md:flex-row gap-4 items-center max-w-3xl mx-auto">
                <select class="flex-1 bg-transparent text-lg font-medium outline-none cursor-pointer px-4">
                    <option>From: China</option>
                    <option>From: Japan</option>
                </select>
                <div class="hidden md:block w-px h-8 bg-gray-300"></div>
                <select class="flex-1 bg-transparent text-lg font-medium outline-none cursor-pointer px-4">
                    <option>To: USA</option>
                </select>
                <div class="hidden md:block w-px h-8 bg-gray-300"></div>
                <select class="flex-1 bg-transparent text-lg font-medium outline-none cursor-pointer px-4">
                    <option>Pet: Cat</option>
                    <option>Pet: Dog</option>
                </select>
                <button class="w-full md:w-auto bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-8 rounded-full transition">Search</button>
            </div>
        </div>
    </div>

    <div class="max-w-5xl mx-auto px-6 py-16">
        <h2 class="text-2xl font-bold text-gray-900 mb-8">Popular Routes</h2>
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {cards_html}
        </div>
    </div>
    """
    html = BASE_HTML_START.format(title="PetEntryGuide | Global Pet Relocation Database", description="Find official pet import requirements.", slug="") + content + BASE_HTML_END
    
    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(html)

def generate_sitemap():
    """生成 sitemap.xml"""
    urls = "<url><loc>https://petentryguide.com/</loc><priority>1.0</priority></url>\n"
    for route in ROUTES_DATA:
        urls += f"<url><loc>https://petentryguide.com/{route['slug']}.html</loc><priority>0.8</priority></url>\n"
    
    sitemap = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>'
    
    with open("public/sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap)

# ==========================================
# 4. 执行控制
# ==========================================
if __name__ == "__main__":
    if not os.path.exists("public"):
        os.makedirs("public")
    
    print("Initializing Static Build Process...")
    
    # 增加数据校验逻辑，防止空表格报错
    if not ROUTES_DATA:
        print("构建中止：没有从 routes.csv 读取到有效数据，请检查文件。")
    else:
        generate_home_page()
        for route in ROUTES_DATA:
            generate_guide_page(route)
            print(f"Generated: /{route['slug']}")
            
        generate_sitemap()
        print("Build Complete. Outputs located in /public directory.")
