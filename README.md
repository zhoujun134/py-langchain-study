# py-langchain-study
langchain 学习笔记

## 使用说明
1. 克隆项目
```shell
git clone git@github.com:zhoujun134/py-langchain-study.git
```

2. 安装依赖包
```shell
pip install -r requirements.txt
```
3. 修改配置文件 .env
```shell
## 智谱 大语言免费模型
#ZHIPU_API_KEY=自己的 api key，通过 https://bigmodel.cn/usercenter/proj-mgmt/apikeys 获取
#ZHIPU_BASE_URL=https://open.bigmodel.cn/api/paas/v4
# 聊天免费模型
#ZHIPU_CHAT_MODEL_NAME=glm-4-flash-250414
## ollama 本地模型配置
#OLLAMA_API_KEY=1111
#OLLAMA_BASE_URL=http://localhost:11434
#OLLAMA_CHAT_MODEL_NAME=qwen3:4b
```
4. 运行项目
```shell
cd test
python test.py
```
