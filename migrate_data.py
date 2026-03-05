import csv
import os

def migrate():
    # 1. 读取旧的杂乱数据
    old_file = 'topics.csv'
    new_file = 'routes.csv'
    
    if not os.path.exists(old_file):
        print("Error: Could not find topics.csv")
        return

    migrated_count = 0
    with open(old_file, 'r', encoding='utf-8') as f_in, \
         open(new_file, 'w', encoding='utf-8', newline='') as f_out:
        
        reader = csv.DictReader(f_in)
        # 严格匹配新版 generate_site.py 所需的表头
        fieldnames = [
            'from_country', 'to_country', 'pet_type', 'title', 'summary', 
            'risk_level', 'prep_time', 'quarantine', 'min_age', 
            'microchip', 'rabies_vaccine', 'process_steps', 
            'required_documents', 'tips'
        ]
        writer = csv.DictWriter(f_out, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            slug = row.get('slug', '')
            content = row.get('content', '')
            title = row.get('title', '')

            # 逻辑：从 slug 提取结构化信息
            if '-to-' not in slug: continue
            parts = slug.split('-to-')
            origin = parts[0]
            dest_pet = parts[1].split('-')
            dest = dest_pet[0]
            pet = dest_pet[1] if len(dest_pet) > 1 else 'pet'

            # 智能研判逻辑：根据关键字判定风险等级
            risk = "High-Risk" if "CDC" in content or "titer" in content.lower() else "Standard"
            prep = "6 Months" if risk == "High-Risk" else "30 Days"
            quarantine = "Required" if "quarantine" in content.lower() and "no quarantine" not in content.lower() else "None"

            # 文本清洗：将大段文字按句号或换行切分为步骤
            clean_text = content.replace('<p>', '').replace('</p>', '').replace('<strong>', '').replace('</strong>', '')
            steps = [s.strip() for s in clean_text.split('.') if len(s.strip()) > 10][:5]
            process_steps = "|".join([f"Step: {s}" for s in steps])

            # 写入新表格
            writer.writerow({
                'from_country': origin,
                'to_country': dest,
                'pet_type': pet,
                'title': title,
                'summary': f"Professional 2026 guide for moving your {pet} from {origin} to {dest}.",
                'risk_level': risk,
                'prep_time': prep,
                'quarantine': quarantine,
                'min_age': "6 Months",
                'microchip': "ISO 11784/85",
                'rabies_vaccine': "Required",
                'process_steps': process_steps,
                'required_documents': "Health Certificate|Rabies Certificate",
                'tips': "Verify all documents with local customs 10 days before departure."
            })
            migrated_count += 1

    print(f"✅ Success! Migrated {migrated_count} routes to routes.csv")

if __name__ == "__main__":
    migrate()
