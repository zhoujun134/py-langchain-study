from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

from com.aiModel.zhi_pu import ZhiPuChatModel

# 2. 创建记忆组件（默认保存全部历史）
memory = ConversationBufferMemory()

# 加载环境变量
load_dotenv()
# 创建模型实例
kModel = ZhiPuChatModel()
# print(f"调用结果为: {llm.chat("您好，你是谁？")} ")
# 3. 创建对话链
conversation = ConversationChain(llm=kModel.llm, memory=memory, verbose=True)

# 4. 进行对话
print(conversation.invoke("我叫zhoujun，我喜欢蓝色请记住我的名字？"))
print(conversation.invoke("还记得我叫什么名字吗？"))
print(conversation.invoke("我最喜欢的颜色是什么"))

# 只保留最近 N 轮（避免历史过长）
# from langchain.memory import ConversationBufferWindowMemory
# memory = ConversationBufferWindowMemory(k=3)  # 只保留最近 3 轮
# 按 Token 数限制（防止超限） 当历史超过 500 token 时，自动把早期对话总结为摘要，再拼接最近完整对话
# from langchain.memory import ConversationTokenBufferMemory
# memory = ConversationTokenBufferMemory(llm=kModel.llm, max_token_limit=500)


# 与 LangGraph 结合：持久化 + 线程级隔离
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import MessagesState, StateGraph
from langchain_core.messages import HumanMessage, AIMessage


# 1. 定义状态
class State(MessagesState):
    pass


# 2. 构建图
def model_node(state: State):
    response = kModel.llm.invoke(state["messages"])
    return {"messages": [AIMessage(content=response.content)]}


builder = StateGraph(State)
builder.add_node("model", model_node)
builder.add_edge("__start__", "model")
builder.add_edge("model", "__end__")

# 3. 添加持久化检查点
memory_checkpointer = MemorySaver()
graph = builder.compile(checkpointer=memory_checkpointer)

# 4. 连续对话（通过 thread_id 隔离上下文）
config = {"configurable": {"thread_id": "user-123"}}
print(f"test 1 {graph.invoke({"messages": [HumanMessage(content="我叫小明")]}, config=config)}")
print(f"test 2 {graph.invoke({"messages": [HumanMessage(content="我喜欢蓝色")]}, config=config)}")
print(f"test 3 {graph.invoke({"messages": [HumanMessage(content="还记得我吗？我最喜欢的颜色是什么")]}, config=config)}")
