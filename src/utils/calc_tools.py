"""
calc_tools - 
Date:2026/9/7
"""
# src/utils/calc_tools.py
"""多参数计算工具模块（结合 *args 与 logger）."""
from src.utils.logger import get_logger


# ... existing code ...
log = get_logger(__name__, "logs/app.log")


def calc_sum(*nums: float) -> float:
    """计算任意数量数字的和，非数字报错并返回 0."""
    try:
        return sum(nums)
    except TypeError as e:
        log.error("calc_sum 入参非数字: %s", e)
        return 0.0


def calc_average(*nums: float) -> float | None:
    """计算平均值，无入参返回 None."""
    if not nums:
        return None
    return calc_sum(*nums) / len(nums)


def calc_stats(*nums: float) -> dict:
    """返回 count/sum/avg/max/min 五项统计."""
    if not nums:
        return {"count": 0, "sum": 0, "avg": None, "max": None, "min": None}
    return {
        "count": len(nums),
        "sum": sum(nums),
        "avg": sum(nums) / len(nums),
        "max": max(nums),
        "min": min(nums),
    }


def weighted_average(values: list[float], weights: list[float]) -> float:
    """加权平均，长度不一致或权重为 0 抛 ValueError."""
    if len(values) != len(weights):
        raise ValueError("values 与 weights 长度不一致")
    if sum(weights) == 0:
        raise ValueError("权重总和不能为 0")
    return sum(v * w for v, w in zip(values, weights)) / sum(weights)


if __name__ == "__main__":
    log.info("stats=%s", calc_stats(10, 20, 30, 40, 50))
    log.info("avg=%s", calc_average(1, 2, 3))
    log.info("weighted=%s", weighted_average([90, 85, 95], [0.3, 0.3, 0.4]))
    calc_sum(1, "abc", 3)   # 故意触发异常分支