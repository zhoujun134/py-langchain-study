import os
from os import environ
from dotenv import load_dotenv

"""
"""
# 加载 .env 文件
load_dotenv()


def get_by_env(key: str) -> str:
    """
        环境变量读取工具类
        1. 优先加载 .env 中的环境变量
        2. 其次读取系统变量的环境变量
    :param key: 环境变量 key 值
    :return: key 对应的环境变量值
    """
    value = environ.get(key)
    if value is None or value == '':
        value = os.getenv(key)
    if value is None or value == '':
        print(f"环境变量中的 {key} 的值为空")
    return value
