from datetime import datetime


def get_current_date() -> str:
    """
    获取当前时间
    :return: YYYY-MM-DD HH:MM:SS.mmm
    """
    # 获取当前时间
    now = datetime.now()
    # 将微秒转换为毫秒，并保留后3位
    milliseconds = now.microsecond // 1000
    # 使用 f-string 格式化当前时间
    formatted_time = (f"{now.year}-{now.month:02d}-{now.day:02d}"
                      f" {now.hour:02d}:{now.minute:02d}:{now.second:02d}.{milliseconds:03d}")
    return formatted_time
