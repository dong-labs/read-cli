"""stats 命令 - 统计摘录概览"""

from read.db.utils import get_stats


def cmd_stats() -> dict:
    """获取统计概览

    Returns:
        统计数据
    """
    stats_data = get_stats()
    return {
        "success": True,
        "data": stats_data,
    }
