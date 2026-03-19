"""tags 命令 - 列出所有标签及数量"""

from read.db.utils import count_by_tag


def cmd_tags() -> dict:
    """列出所有标签及使用数量

    Returns:
        标签统计数据
    """
    tag_counts = count_by_tag()

    # 按数量排序
    sorted_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)
    tags_list = [{"tag": tag, "count": count} for tag, count in sorted_tags]

    return {
        "success": True,
        "data": {
            "total_tags": len(tag_counts),
            "total_usages": sum(tag_counts.values()),
            "tags": tags_list,
        }
    }
