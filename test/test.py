from com.aiModel.ollama_qwen import QWenChatModel
from com.aiModel.zhi_pu import ZhiPuChatModel

from com.utils.date_utls import get_current_date
import os
from os import environ
from dotenv import load_dotenv
import json

print(environ.values())

# 开始调用
ollama_qwen = QWenChatModel(model_name="qwen3:4b")
# ollama_qwen = QWenChatModel(model_name="deepseek-r1:8b")
print(f"开始调用时间 ollama_qwen: {get_current_date()}")
print(ollama_qwen.chat('请使用 java 编写一个快速排序', think=False))
print(f"结束调用时间 ollama_qwen: {get_current_date()}")
#
# zhi_pu_model = ZhiPuChatModel()
# print(f"开始调用时间 zhi_pu_model: {get_current_date()}")
# print(zhi_pu_model.chat('请将下面这段代码翻译成C语言：print("Hello World")'))
# print(f"结束调用时间 zhi_pu_model: {get_current_date()}")
