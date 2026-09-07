"""
data_cleaner - 
Date:2026/9/4
"""
# src/services/data_cleaner.py
"""数据清洗与统计脚本（综合今天所学）."""
import sys
import os
from typing import List

# 将项目根目录添加到 sys.path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# src/services/data_cleaner.py
"""数据清洗与统计脚本（综合今天所学）."""
from src.utils.logger import get_logger

log = get_logger(__name__, "logs/app.log")


def clean_lines(path: str) -> list[str]:
    """读文件，去空行、去前后空格、去重，保持原顺序."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = f.readlines()
    except FileNotFoundError:
        log.error("文件不存在: %s", path)
        return []

    seen, result = set(), []
    for line in raw:
        s = line.strip()
        if not s or s in seen:
            continue
        seen.add(s)
        result.append(s)

    log.info("原始 %d 行 → 清洗后 %d 行", len(raw), len(result))
    return result


def group_by_city(rows: list[tuple[str, str]]) -> dict[str, int]:
    """按城市分组统计."""
    stats = {}
    for _, city in rows:
        stats[city] = stats.get(city, 0) + 1
    return stats


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))

    # 构建正确的文件路径
    file_path = os.path.join(project_root, "data", "raw", "users.txt")

    lines = clean_lines(file_path)
    log.info("去重后样例: %s", lines[:3])

    students = [("张三", "北京"), ("李四", "上海"), ("王五", "北京")]
    log.info("城市分组: %s", group_by_city(students))

    team_a = {1,2,3,4,5,6,7,8,9}
    team_b = {2,4,6,8}
    print(f"team_a和team_b的交集{team_a & team_b}")
    print(f"team_a和team_b的交集{team_a.intersection(team_b)}")
    print(f'team_a和team_b的差集{team_a.difference(team_b)}')
    print(f'team_a和team_b的差集{team_b.difference(team_a)}')