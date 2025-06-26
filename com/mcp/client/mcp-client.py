# mcp_client.py
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent


from dotenv import load_dotenv

from com.aiModel.ollama_qwen import QWenChatModel

# 加载环境变量
load_dotenv()
# 1. 初始化 LLM
llm = QWenChatModel().llm


async def main():
    # 2. 连接到 MCP Server
    client = MultiServerMCPClient({
        "math": {
            "command": "python",
            "args": ["../server/math_mcp_server.py"],
            "transport": "stdio"
        }
    })

    # 3. 获取工具
    tools = await client.get_tools()
    print("Available tools:", [t.name for t in tools])

    # 4. 创建 ReAct Agent
    agent = create_react_agent(llm, tools)

    # 5. 交互循环
    while True:
        user_input = input("\n请输入问题（或输入 'exit' 退出）：").strip()
        if user_input.lower() == "exit":
            print("再见！")
            break

        # 6. 调用 Agent
        response = await agent.ainvoke({"messages": "/no_think" + user_input})
        print("最终答案:", response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
