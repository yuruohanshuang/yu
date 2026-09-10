"""
data_cleaner - 
Date:2026/9/4
"""
# src/services/data_cleaner.py
"""数据清洗与统计脚本（综合今天所学）."""
import sys
import os
from typing import List
import os
from collections.abc import Iterator

# 将项目根目录添加到 sys.path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

"""数据清洗与统计脚本（生成器管道版）."""

from src.utils.logger import get_logger
log = get_logger(__name__, "logs/app.log")

# ---------- 管道各阶段：每个都是生成器 ----------

def read_lines(path: str) -> Iterator[str]:
    """阶段 1：惰性逐行读取（文件对象本身就是迭代器，不会一次性读入）."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            yield from f          # 关键：不 readlines()，逐行产出
    except FileNotFoundError:
        log.error("文件不存在: %s", path)
        return


def strip_lines(lines: Iterator[str]) -> Iterator[str]:
    """阶段 2：去首尾空白."""
    for line in lines:
        yield line.strip()


def filter_empty(lines: Iterator[str]) -> Iterator[str]:
    """阶段 3：过滤空行."""
    for s in lines:
        if s:
            yield s


def dedup(lines: Iterator[str]) -> Iterator[str]:
    """
    阶段 4：去重（保持原顺序）.
    注意：seen 集合仍需 O(唯一行数) 内存——去重本身不可避免要"记住见过的".
    如果唯一行太多导致内存爆，见下文『进阶方案』.
    """
    seen: set[str] = set()
    for s in lines:
        if s not in seen:
            seen.add(s)
            yield s


def clean_lines(path: str) -> Iterator[str]:
    """用生成器管道组合：读 → strip → 去空 → 去重. 全程惰性."""
    pipeline = dedup(filter_empty(strip_lines(read_lines(path))))
    return pipeline

def group_by_city(rows: list[tuple[str, str]]) -> dict[str, int]:
    """按城市分组统计."""
    stats = {}
    for _, city in rows:
        stats[city] = stats.get(city, 0) + 1
    return stats

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))
    file_path = os.path.join(project_root, "data", "raw", "users.txt")

    # 只要前 3 行？—— 生成器只读到第 3 行就停，GB 文件瞬间返回
    from itertools import islice
    sample = list(islice(clean_lines(file_path), 3))
    log.info("去重后样例: %s", sample)

    # 想统计总数？—— 流式累加，不保存所有行
    total = sum(1 for _ in clean_lines(file_path))
    log.info("清洗后总行数: %d", total)

    # 想写到另一个文件？—— 边流边写，内存恒定
    with open("cleaned.txt", "w", encoding="utf-8") as out:
        for line in clean_lines(file_path):
            out.write(line + "\n")