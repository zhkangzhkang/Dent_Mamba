import os
from pathlib import Path
from collections import Counter, defaultdict

def count_global_instances(label_dir):
    label_path = Path(label_dir)
    
    # 1. 初始化计数器
    instance_counts = Counter()      # 统计每个类别有多少个框 (Instance)
    file_counts = defaultdict(int)   # 统计每个类别出现在多少张图片中 (Image Count)
    total_files = 0
    empty_files = 0

    print(f"正在扫描: {label_dir} ...")

    # 2. 遍历所有 txt
    files = list(label_path.glob("*.txt"))
    total_files = len(files)

    for file_path in files:
        is_empty = True
        seen_classes_in_this_file = set() # 用于去重，统计文件数

        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 1:
                    is_empty = False
                    class_id = parts[0] # 获取类别ID
                    
                    # 统计实例数 (有多少个框)
                    instance_counts[class_id] += 1
                    
                    # 记录该文件包含的类别 (用于统计文件数)
                    seen_classes_in_this_file.add(class_id)
        
        if is_empty:
            empty_files += 1
        
        # 统计文件分布
        for cid in seen_classes_in_this_file:
            file_counts[cid] += 1

    # --- 3. 打印精美报表 ---
    print("\n" + "="*50)
    print(f"📊 数据集标签统计报告")
    print(f"📂 目录: {label_path.name}")
    print(f"📄 总文件数: {total_files}")
    print(f"🚫 空文件数 (无标签): {empty_files}")
    print("="*50)
    
    print(f"{'ID':<6} | {'实例总数(框)':<12} | {'图片覆盖数(张)':<12} | {'占比(%)':<8}")
    print("-" * 50)

    if not instance_counts:
        print("未发现任何标签数据！")
        return

    # 计算总框数用于算百分比
    total_instances = sum(instance_counts.values())

    # 按类别ID数字大小排序输出 (例如 0, 1, 2, 10...)
    sorted_keys = sorted(instance_counts.keys(), key=lambda x: int(x) if x.isdigit() else x)

    for cls_id in sorted_keys:
        count = instance_counts[cls_id]
        file_count = file_counts[cls_id]
        percent = (count / total_files) * 100 if total_files > 0 else 0 # 这里算的是覆盖率，或者用 total_instances 算类别占比
        
        # 计算该类别占所有框的百分比
        ratio = (count / total_instances) * 100
        
        print(f"{cls_id:<6} | {count:<12} | {file_count:<12} | {ratio:.2f}%")

    print("="*50)
    print(f"∑ 所有标签总数: {total_instances}")
    print("="*50)

# ================= 配置区域 =================
# 修改这里的路径为你存放 txt 标签的文件夹
TARGET_FOLDER = r"C:\Users\zk\Desktop\xiaoyaxunlian\1_disease_crops - V1\labels11" 

if __name__ == "__main__":
    count_global_instances(TARGET_FOLDER)