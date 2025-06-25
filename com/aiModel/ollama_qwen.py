from langchain_core.messages import BaseMessage, SystemMessage, HumanMessage
from langchain_ollama import ChatOllama

from com.aiModel.base_model import ZBaseChatModel
from com.utils.env_utils import get_by_env


class QWenChatModel(ZBaseChatModel):
    """
    智谱聊天模型
    """

    def __init__(self, api_key: str = None,
                 base_url: str = None,
                 model_name: str = None,
                 default_headers: dict = None,
                 systemMessage: SystemMessage = SystemMessage(content="")):
        if default_headers is None:
            default_headers = {"Content-Type": "application/json"}
        if api_key is None:
            api_key = get_by_env("OLLAMA_BASE_URL")
        if base_url is None:
            base_url = get_by_env("OLLAMA_BASE_URL")
        if model_name is None:
            model_name = get_by_env("OLLAMA_CHAT_MODEL_NAME")
        self.api_key = api_key
        self.base_url = base_url
        self.model_name = model_name
        self.default_headers = default_headers
        self.systemMessage = systemMessage
        super().__init__(api_key=self.api_key, base_url=self.base_url,
                         model_name=self.model_name,
                         default_headers=self.default_headers,
                         belong_openai_model=False)
        self.llm = ChatOllama(base_url=self.base_url,
                              api_key=self.api_key,
                              model=self.model_name,
                              default_headers=self.default_headers)

    def chat(self, question: str = '', think: bool = False) -> BaseMessage:
        if think:
            self.systemMessage = SystemMessage(content="/think \n" + self.systemMessage.content)
        else:
            self.systemMessage = SystemMessage(content="/no_think \n" + self.systemMessage.content)
        message = [self.systemMessage,
                   HumanMessage(content=question)]
        response: BaseMessage = self.llm.invoke(message, stream=False, think=False)
        return response
